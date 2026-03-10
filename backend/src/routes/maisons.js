'use strict';

const { Router } = require('express');
const { getAll, getFeatured, getOne, create, update, remove } = require('../controllers/maisonController');
const { protect } = require('../middleware/authMiddleware');

const router = Router();

router.get('/featured', getFeatured);
router.get('/', getAll);
router.get('/:id', getOne);

router.post('/', protect, create);
router.put('/:id', protect, update);
router.delete('/:id', protect, remove);

module.exports = router;
