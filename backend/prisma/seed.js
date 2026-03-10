'use strict';

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
