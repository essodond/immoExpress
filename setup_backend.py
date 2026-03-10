"""Setup script to create the complete Express.js backend for the immo real estate platform."""
import os

BASE = r"C:\Users\DELL\Documents\projet\immo\backend"

DIRS = [
    BASE,
    os.path.join(BASE, "src"),
    os.path.join(BASE, "src", "utils"),
    os.path.join(BASE, "src", "middleware"),
    os.path.join(BASE, "src", "controllers"),
    os.path.join(BASE, "src", "routes"),
    os.path.join(BASE, "prisma"),
]

FILES = {}

FILES[os.path.join(BASE, "package.json")] = '''{
  "name": "immo-backend",
  "version": "1.0.0",
  "description": "Real estate platform backend API",
  "main": "src/server.js",
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js",
    "db:migrate": "prisma migrate dev",
    "db:generate": "prisma generate",
    "db:seed": "node prisma/seed.js"
  },
  "dependencies": {
    "@prisma/client": "^5.0.0",
    "bcryptjs": "^2.4.3",
    "cloudinary": "^1.41.0",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "express-rate-limit": "^7.1.5",
    "helmet": "^7.1.0",
    "jsonwebtoken": "^9.0.2",
    "morgan": "^1.10.0",
    "multer": "^1.4.5-lts.1",
    "zod": "^3.22.4"
  },
  "devDependencies": {
    "nodemon": "^3.0.2",
    "prisma": "^5.0.0"
  }
}
'''

FILES[os.path.join(BASE, ".env.example")] = '''DATABASE_URL="postgresql://user:password@localhost:5432/immo_db"
JWT_SECRET="your-secret-key-here"
JWT_EXPIRES_IN="7d"
CLOUDINARY_CLOUD_NAME="your-cloud-name"
CLOUDINARY_API_KEY="your-api-key"
CLOUDINARY_API_SECRET="your-api-secret"
FRONTEND_URL="http://localhost:3000"
PORT=5000
'''

FILES[os.path.join(BASE, ".gitignore")] = '''node_modules/
.env
dist/
*.log
.DS_Store
'''

FILES[os.path.join(BASE, "prisma", "schema.prisma")] = '''generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Maison {
  id          String   @id @default(cuid())
  titre       String
  description String
  prix        Float
  type        String
  ville       String
  quartier    String
  chambres    Int
  sallesBain  Int
  superficie  Float
  statut      String   @default("disponible")
  videoUrl    String?
  photos      Photo[]
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

model Photo {
  id        String   @id @default(cuid())
  url       String
  publicId  String
  isMain    Boolean  @default(false)
  maison    Maison   @relation(fields: [maisonId], references: [id], onDelete: Cascade)
  maisonId  String
  createdAt DateTime @default(now())
}

model Admin {
  id        String   @id @default(cuid())
  email     String   @unique
  password  String
  nom       String
  createdAt DateTime @default(now())
}
'''

FILES[os.path.join(BASE, "prisma", "seed.js")] = """'use strict';

const { PrismaClient } = require('@prisma/client');
const bcrypt = require('bcryptjs');

const prisma = new PrismaClient();

async function main() {
  const existingAdmin = await prisma.admin.findUnique({
    where: { email: 'admin@immo.com' },
  });

  if (existingAdmin) {
    console.log('Admin already exists, skipping seed.');
    return;
  }

  const hashedPassword = await bcrypt.hash('Admin123!', 12);

  const admin = await prisma.admin.create({
    data: {
      email: 'admin@immo.com',
      password: hashedPassword,
      nom: 'Administrateur',
    },
  });

  console.log('Default admin created:', { id: admin.id, email: admin.email });
}

main()
  .catch((e) => {
    console.error('Seed error:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
"""

FILES[os.path.join(BASE, "src", "utils", "cloudinary.js")] = """'use strict';

const cloudinary = require('cloudinary').v2;

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

const uploadBuffer = (buffer, folder = 'immo/maisons') => {
  return new Promise((resolve, reject) => {
    const uploadStream = cloudinary.uploader.upload_stream(
      {
        folder,
        resource_type: 'image',
        transformation: [
          { width: 1280, height: 720, crop: 'limit', quality: 'auto:good' },
        ],
      },
      (error, result) => {
        if (error) return reject(error);
        resolve({ url: result.secure_url, publicId: result.public_id });
      }
    );
    uploadStream.end(buffer);
  });
};

const deleteResource = async (publicId) => {
  return cloudinary.uploader.destroy(publicId);
};

module.exports = { uploadBuffer, deleteResource };
"""

FILES[os.path.join(BASE, "src", "utils", "jwt.js")] = """'use strict';

const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET;
const EXPIRES_IN = process.env.JWT_EXPIRES_IN || '7d';

if (!SECRET) {
  throw new Error('JWT_SECRET environment variable is not set');
}

const signToken = (payload) => {
  return jwt.sign(payload, SECRET, { expiresIn: EXPIRES_IN });
};

const verifyToken = (token) => {
  return jwt.verify(token, SECRET);
};

module.exports = { signToken, verifyToken };
"""

FILES[os.path.join(BASE, "src", "middleware", "authMiddleware.js")] = """'use strict';

const { verifyToken } = require('../utils/jwt');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

const protect = async (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({ success: false, message: 'Non autorisé. Token manquant.' });
    }

    const token = authHeader.split(' ')[1];
    const decoded = verifyToken(token);

    const admin = await prisma.admin.findUnique({
      where: { id: decoded.id },
      select: { id: true, email: true, nom: true, createdAt: true },
    });

    if (!admin) {
      return res.status(401).json({ success: false, message: 'Admin introuvable.' });
    }

    req.admin = admin;
    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({ success: false, message: 'Token expiré.' });
    }
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({ success: false, message: 'Token invalide.' });
    }
    next(error);
  }
};

module.exports = { protect };
"""

FILES[os.path.join(BASE, "src", "middleware", "validate.js")] = """'use strict';

const validate = (schema) => (req, res, next) => {
  const result = schema.safeParse(req.body);

  if (!result.success) {
    const errors = result.error.errors.map((e) => ({
      field: e.path.join('.'),
      message: e.message,
    }));
    return res.status(422).json({ success: false, message: 'Données invalides.', errors });
  }

  req.validatedBody = result.data;
  next();
};

module.exports = { validate };
"""

FILES[os.path.join(BASE, "src", "middleware", "errorHandler.js")] = """'use strict';

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
"""

FILES[os.path.join(BASE, "src", "controllers", "authController.js")] = """'use strict';

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
"""

FILES[os.path.join(BASE, "src", "controllers", "maisonController.js")] = """'use strict';

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
"""

FILES[os.path.join(BASE, "src", "controllers", "uploadController.js")] = """'use strict';

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

      res.status(201).json({ success: true, count: photos.length, data: photos });
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
"""

FILES[os.path.join(BASE, "src", "routes", "auth.js")] = """'use strict';

const { Router } = require('express');
const { login, refresh, me } = require('../controllers/authController');
const { protect } = require('../middleware/authMiddleware');

const router = Router();

router.post('/login', login);
router.post('/refresh', protect, refresh);
router.get('/me', protect, me);

module.exports = router;
"""

FILES[os.path.join(BASE, "src", "routes", "maisons.js")] = """'use strict';

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
"""

FILES[os.path.join(BASE, "src", "routes", "upload.js")] = """'use strict';

const { Router } = require('express');
const { uploadPhotos, deletePhoto, setMainPhoto } = require('../controllers/uploadController');
const { protect } = require('../middleware/authMiddleware');

const router = Router();

router.post('/photos/:maisonId', protect, uploadPhotos);
router.delete('/photos/:photoId', protect, deletePhoto);
router.put('/photos/:photoId/main', protect, setMainPhoto);

module.exports = router;
"""

FILES[os.path.join(BASE, "src", "server.js")] = """'use strict';

require('dotenv').config();

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');

const authRoutes = require('./routes/auth');
const maisonRoutes = require('./routes/maisons');
const uploadRoutes = require('./routes/upload');
const { errorHandler, notFound } = require('./middleware/errorHandler');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(helmet());

app.use(
  cors({
    origin: ['http://localhost:3000', process.env.FRONTEND_URL].filter(Boolean),
    credentials: true,
  })
);

app.use(morgan(process.env.NODE_ENV === 'production' ? 'combined' : 'dev'));

app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

const publicLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  message: { success: false, message: 'Trop de requêtes. Réessayez dans 15 minutes.' },
});

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 20,
  standardHeaders: true,
  legacyHeaders: false,
  message: { success: false, message: 'Trop de tentatives de connexion. Réessayez dans 15 minutes.' },
});

app.get('/api/health', (req, res) => {
  res.json({ success: true, message: 'API opérationnelle', timestamp: new Date().toISOString() });
});

app.use('/api/auth', authLimiter, authRoutes);
app.use('/api/maisons', publicLimiter, maisonRoutes);
app.use('/api/upload', publicLimiter, uploadRoutes);

app.use(notFound);
app.use(errorHandler);

app.listen(PORT, () => {
  console.log(`\\n🚀 Serveur démarré sur http://localhost:${PORT}`);
  console.log(`📋 Environnement: ${process.env.NODE_ENV || 'development'}`);
  console.log(`🏠 API immobilière prête\\n`);
});

module.exports = app;
"""

created_dirs = []
created_files = []
errors = []

for d in DIRS:
    try:
        os.makedirs(d, exist_ok=True)
        created_dirs.append(d)
        print(f"  DIR  {d}")
    except Exception as e:
        errors.append(f"DIR {d}: {e}")
        print(f"  ERR  {d}: {e}")

for path, content in FILES.items():
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        created_files.append(path)
        print(f"  FILE {path}")
    except Exception as e:
        errors.append(f"FILE {path}: {e}")
        print(f"  ERR  {path}: {e}")

print(f"\n=== SUMMARY ===")
print(f"Directories created : {len(created_dirs)}/{len(DIRS)}")
print(f"Files created       : {len(created_files)}/{len(FILES)}")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors:
        print(f"  {e}")
else:
    print("No errors. Backend scaffold is ready!")
    print(f"\nNext steps:")
    print(f"  cd {BASE}")
    print(f"  npm install")
    print(f"  copy .env.example .env   (then fill in your values)")
    print(f"  npx prisma migrate dev")
    print(f"  npm run dev")
