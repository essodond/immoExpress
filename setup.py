#!/usr/bin/env python3
"""ImmoExpert - Main setup runner.

Run from C:\Users\DELL\Documents\projet\immo\:
    python setup.py

Then:
    cd frontend
    npm install
    copy .env.local.example .env.local
    (edit .env.local with your values)
    npm run dev
"""

import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))

scripts = [
    os.path.join(HERE, 'setup_1.py'),
    os.path.join(HERE, 'setup_2.py'),
    os.path.join(HERE, 'setup_3.py'),
    os.path.join(HERE, 'setup_4.py'),
]

print('\n' + '='*55)
print('  ImmoExpert - Next.js 14 Frontend Setup')
print('='*55 + '\n')

for script in scripts:
    if not os.path.exists(script):
        print(f'ERROR: {script} not found.')
        sys.exit(1)
    with open(script, 'r', encoding='utf-8') as f:
        exec(compile(f.read(), script, 'exec'))

# Create a minimal public placeholder SVG
BASE = r'C:\Users\DELL\Documents\projet\immo\frontend'
ph = os.path.join(BASE, 'public', 'placeholder.svg')
os.makedirs(os.path.join(BASE, 'public'), exist_ok=True)
with open(ph, 'w', encoding='utf-8') as f:
    f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <rect width="800" height="600" fill="#E2E8F0"/>
  <rect x="300" y="180" width="200" height="160" rx="8" fill="#CBD5E1"/>
  <polygon points="280,210 400,140 520,210" fill="#94A3B8"/>
  <rect x="370" y="280" width="60" height="60" rx="4" fill="#94A3B8"/>
  <text x="400" y="410" text-anchor="middle" font-family="sans-serif" font-size="20" fill="#94A3B8">
    Photo non disponible
  </text>
</svg>''')
print('  \u2713 public/placeholder.svg')

print('\n' + '='*55)
print('  All files created successfully!')
print('='*55)
print('\nNext steps:')
print('  1. cd frontend')
print('  2. npm install')
print('  3. copy .env.local.example .env.local')
print('  4. Edit .env.local with your API URL and WhatsApp number')
print('  5. npm run dev')
print('\n  Admin: http://localhost:3000/admin/login')
print('  Site:  http://localhost:3000\n')
