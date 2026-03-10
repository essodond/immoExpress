#!/usr/bin/env node
/**
 * ImmoExpert - Project setup runner
 * Usage: node run_setup.js
 * Requires Python 3 in PATH.
 */
const { execSync } = require('child_process');
const path = require('path');
const fs   = require('fs');

const dir = path.join(__dirname);

// Verify setup scripts exist
const scripts = ['setup_1.py','setup_2.py','setup_3.py','setup_4.py','setup.py'];
for (const s of scripts) {
  if (!fs.existsSync(path.join(dir, s))) {
    console.error(`Missing: ${s}`);
    process.exit(1);
  }
}

console.log('\n=== ImmoExpert Frontend Setup ===\n');
try {
  // setup.py internally calls setup_1..4 via exec(), so just run it once
  execSync('python setup.py', { cwd: dir, stdio: 'inherit' });
} catch (e) {
  // Fallback: run sub-scripts individually in case exec() is not available
  console.log('Fallback: running sub-scripts individually...');
  for (const s of ['setup_1.py','setup_2.py','setup_3.py','setup_4.py']) {
    execSync(`python ${s}`, { cwd: dir, stdio: 'inherit' });
  }
  // Create placeholder
  const pub = path.join(dir, 'frontend', 'public');
  fs.mkdirSync(pub, { recursive: true });
  console.log('Done.');
}
