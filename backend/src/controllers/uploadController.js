'use strict';

const multer = require('multer');
const { PrismaClient } = require('@prisma/client');
const { uploadBuffer, deleteResource } = require('../utils/cloudinary');

const prisma = new PrismaClient();

const storage = multer.memoryStorage();

const fileFilter = (req, file, cb) => {
  const allowed = ['image/jpeg', 'image/png', 'image/webp'];
  if (allowed.includes(file.mimetype)) {
    cb(null, true);
  } else {
    cb(new Error('Format de fichier non supporté. Utilisez JPEG, PNG ou WebP.'), false);
  }
};

const upload = multer({
  storage,
  fileFilter,
  limits: { fileSize: 10 * 1024 * 1024 },
});

const uploadPhotos = [
  upload.array('photos', 10),
  async (req, res, next) => {
    try {
      if (!req.files || req.files.length === 0) {
        return res.status(400).json({ success: false, message: 'Aucune photo fournie.' });
      }

      const maison = await prisma.maison.findUnique({ where: { id: req.params.maisonId } });
      if (!maison) {
        return res.status(404).json({ success: false, message: 'Maison introuvable.' });
      }

      const hasMain = await prisma.photo.findFirst({
        where: { maisonId: req.params.maisonId, isMain: true },
      });

      const uploadResults = await Promise.all(
        req.files.map((file) => uploadBuffer(file.buffer, `immo/maisons/${req.params.maisonId}`))
      );

      const photos = await Promise.all(
        uploadResults.map((result, index) =>
          prisma.photo.create({
            data: {
              url: result.url,
              publicId: result.publicId,
              isMain: !hasMain && index === 0,
              maisonId: req.params.maisonId,
            },
          })
        )
      );

      res.status(201).json({ success: true, message: `${photos.length} photo(s) uploadée(s) avec succès.`, data: photos });
    } catch (error) {
      next(error);
    }
  },
];

const deletePhoto = async (req, res, next) => {
  try {
    const photo = await prisma.photo.findUnique({ where: { id: req.params.photoId } });

    if (!photo) {
      return res.status(404).json({ success: false, message: 'Photo introuvable.' });
    }

    await deleteResource(photo.publicId);
    await prisma.photo.delete({ where: { id: req.params.photoId } });

    if (photo.isMain) {
      const nextPhoto = await prisma.photo.findFirst({
        where: { maisonId: photo.maisonId },
        orderBy: { createdAt: 'asc' },
      });
      if (nextPhoto) {
        await prisma.photo.update({ where: { id: nextPhoto.id }, data: { isMain: true } });
      }
    }

    res.json({ success: true, message: 'Photo supprimée avec succès.' });
  } catch (error) {
    next(error);
  }
};

const setMainPhoto = async (req, res, next) => {
  try {
    const photo = await prisma.photo.findUnique({ where: { id: req.params.photoId } });

    if (!photo) {
      return res.status(404).json({ success: false, message: 'Photo introuvable.' });
    }

    await prisma.$transaction([
      prisma.photo.updateMany({ where: { maisonId: photo.maisonId }, data: { isMain: false } }),
      prisma.photo.update({ where: { id: photo.id }, data: { isMain: true } }),
    ]);

    res.json({ success: true, message: 'Photo principale mise à jour.' });
  } catch (error) {
    next(error);
  }
};

module.exports = { uploadPhotos, deletePhoto, setMainPhoto };
