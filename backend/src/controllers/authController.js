'use strict';

const bcrypt = require('bcryptjs');
const { PrismaClient } = require('@prisma/client');
const { signToken } = require('../utils/jwt');

const prisma = new PrismaClient();

const login = async (req, res, next) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ success: false, message: 'Email et mot de passe requis.' });
    }

    const admin = await prisma.admin.findUnique({ where: { email } });

    if (!admin || !(await bcrypt.compare(password, admin.password))) {
      return res.status(401).json({ success: false, message: 'Identifiants invalides.' });
    }

    const token = signToken({ id: admin.id, email: admin.email });

    res.json({
      success: true,
      token,
      admin: { id: admin.id, email: admin.email, nom: admin.nom },
    });
  } catch (error) {
    next(error);
  }
};

const refresh = async (req, res, next) => {
  try {
    const token = signToken({ id: req.admin.id, email: req.admin.email });
    res.json({ success: true, token });
  } catch (error) {
    next(error);
  }
};

const me = (req, res) => {
  res.json({ success: true, admin: req.admin });
};

module.exports = { login, refresh, me };
