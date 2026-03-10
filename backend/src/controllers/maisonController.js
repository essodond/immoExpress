'use strict';

const { PrismaClient } = require('@prisma/client');
const { z } = require('zod');
const { deleteResource } = require('../utils/cloudinary');

const prisma = new PrismaClient();

const maisonSchema = z.object({
  titre: z.string().min(3).max(200),
  description: z.string().min(10),
  prix: z.number().positive(),
  type: z.enum(['vente', 'location']),
  ville: z.string().min(2),
  quartier: z.string().min(2),
  chambres: z.number().int().min(0),
  sallesBain: z.number().int().min(0),
  superficie: z.number().positive(),
  statut: z.enum(['disponible', 'vendu', 'loue']).optional().default('disponible'),
  videoUrl: z.string().url().optional().nullable(),
});

const getAll = async (req, res, next) => {
  try {
    const { ville, type, prixMin, prixMax, chambres, statut } = req.query;

    const where = {};
    if (ville) where.ville = { contains: ville, mode: 'insensitive' };
    if (type) where.type = type;
    if (statut) where.statut = statut;
    if (chambres) where.chambres = { gte: parseInt(chambres, 10) };
    if (prixMin || prixMax) {
      where.prix = {};
      if (prixMin) where.prix.gte = parseFloat(prixMin);
      if (prixMax) where.prix.lte = parseFloat(prixMax);
    }

    const maisons = await prisma.maison.findMany({
      where,
      include: { photos: { orderBy: { isMain: 'desc' } } },
      orderBy: { createdAt: 'desc' },
    });

    res.json({ success: true, count: maisons.length, data: maisons });
  } catch (error) {
    next(error);
  }
};

const getFeatured = async (req, res, next) => {
  try {
    const maisons = await prisma.maison.findMany({
      where: { statut: 'disponible' },
      include: { photos: { where: { isMain: true }, take: 1 } },
      orderBy: { createdAt: 'desc' },
      take: 6,
    });

    res.json({ success: true, data: maisons });
  } catch (error) {
    next(error);
  }
};

const getOne = async (req, res, next) => {
  try {
    const maison = await prisma.maison.findUnique({
      where: { id: req.params.id },
      include: { photos: { orderBy: { isMain: 'desc' } } },
    });

    if (!maison) {
      return res.status(404).json({ success: false, message: 'Maison introuvable.' });
    }

    res.json({ success: true, data: maison });
  } catch (error) {
    next(error);
  }
};

const create = async (req, res, next) => {
  try {
    const result = maisonSchema.safeParse(req.body);
    if (!result.success) {
      const errors = result.error.errors.map((e) => ({ field: e.path.join('.'), message: e.message }));
      return res.status(422).json({ success: false, message: 'Données invalides.', errors });
    }

    const maison = await prisma.maison.create({ data: result.data });
    res.status(201).json({ success: true, data: maison });
  } catch (error) {
    next(error);
  }
};

const update = async (req, res, next) => {
  try {
    const result = maisonSchema.partial().safeParse(req.body);
    if (!result.success) {
      const errors = result.error.errors.map((e) => ({ field: e.path.join('.'), message: e.message }));
      return res.status(422).json({ success: false, message: 'Données invalides.', errors });
    }

    const maison = await prisma.maison.update({
      where: { id: req.params.id },
      data: result.data,
    });

    res.json({ success: true, data: maison });
  } catch (error) {
    next(error);
  }
};

const remove = async (req, res, next) => {
  try {
    const maison = await prisma.maison.findUnique({
      where: { id: req.params.id },
      include: { photos: true },
    });

    if (!maison) {
      return res.status(404).json({ success: false, message: 'Maison introuvable.' });
    }

    if (maison.photos.length > 0) {
      await Promise.allSettled(maison.photos.map((p) => deleteResource(p.publicId)));
    }

    await prisma.maison.delete({ where: { id: req.params.id } });

    res.json({ success: true, message: 'Maison supprimée avec succès.' });
  } catch (error) {
    next(error);
  }
};

module.exports = { getAll, getFeatured, getOne, create, update, remove };
