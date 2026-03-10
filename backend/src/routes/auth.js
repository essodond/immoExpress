'use strict';

const { Router } = require('express');
const { login, refresh, me } = require('../controllers/authController');
const { protect } = require('../middleware/authMiddleware');

const router = Router();

router.post('/login', login);
router.post('/refresh', protect, refresh);
router.get('/me', protect, me);

module.exports = router;
