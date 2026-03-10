const fs = require('fs');
const path = require('path');

const dirs = [
  'frontend/src/app/catalogue',
  'frontend/src/app/maison/[id]',
  'frontend/src/app/a-propos',
  'frontend/src/app/admin/login',
  'frontend/src/app/admin/dashboard',
  'frontend/src/app/admin/maisons/nouvelle',
  'frontend/src/app/admin/maisons/[id]',
  'frontend/src/components/layout',
  'frontend/src/components/maison',
  'frontend/src/components/ui',
  'frontend/src/lib',
  'frontend/src/types',
  'frontend/src/providers',
  'frontend/public'
];

const baseDir = 'C:\\Users\\DELL\\Documents\\projet\\immo';

dirs.forEach(dir => {
  const fullPath = path.join(baseDir, dir);
  try {
    fs.mkdirSync(fullPath, { recursive: true });
    console.log(`✓ Created: ${fullPath}`);
  } catch (err) {
    console.error(`✗ Error creating ${fullPath}:`, err.message);
  }
});

console.log('\n✓ Directory structure created successfully!');
