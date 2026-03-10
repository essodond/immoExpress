'use strict';

const { Router } = require('express');
const { uploadPhotos, deletePhoto, setMainPhoto } = require('../controllers/uploadController');
const { protect } = require('../middleware/authMiddleware');

const router = Router();

router.post('/photos/:maisonId', protect, uploadPhotos);
router.delete('/photos/:photoId', protect, deletePhoto);
router.put('/photos/:photoId/main', protect, setMainPhoto);

module.exports = router;
