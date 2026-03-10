'use strict';

const errorHandler = (err, req, res, next) => {
  console.error(`[${new Date().toISOString()}] ERROR:`, err);

  if (err.code === 'P2002') {
    return res.status(409).json({ success: false, message: 'Une valeur unique existe déjà.' });
  }
  if (err.code === 'P2025') {
    return res.status(404).json({ success: false, message: 'Ressource introuvable.' });
  }

  const statusCode = err.statusCode || err.status || 500;
  const message = err.message || 'Erreur interne du serveur.';

  res.status(statusCode).json({
    success: false,
    message,
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack }),
  });
};

const notFound = (req, res) => {
  res.status(404).json({ success: false, message: `Route introuvable: ${req.method} ${req.originalUrl}` });
};

module.exports = { errorHandler, notFound };
