#!/usr/bin/env python
"""Create Next.js project directory structure"""

import os

basePath = r'C:\Users\DELL\Documents\projet\immo\frontend'
dirs = [
    r'src\app\catalogue',
    r'src\app\maison\[id]',
    r'src\app\a-propos',
    r'src\app\admin\login',
    r'src\app\admin\dashboard',
    r'src\app\admin\maisons\nouvelle',
    r'src\app\admin\maisons\[id]',
    r'src\components\layout',
    r'src\components\maison',
    r'src\components\ui',
    r'src\lib',
    r'src\types',
    r'src\providers',
    r'public'
]

created_count = 0
for dir_path in dirs:
    full_path = os.path.join(basePath, dir_path)
    try:
        os.makedirs(full_path, exist_ok=True)
        created_count += 1
        print(f"✓ Created: {dir_path}")
    except Exception as e:
        print(f"✗ Failed to create {dir_path}: {e}")

print(f"\n✓ Successfully created {created_count}/{len(dirs)} directories")
