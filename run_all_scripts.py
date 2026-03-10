#!/usr/bin/env python3
import subprocess
import sys
import os

os.chdir(r'C:\Users\DELL\Documents\projet\immo')

print("=" * 50)
print("Running setup_backend.py...")
print("=" * 50)
result1 = subprocess.run([sys.executable, 'setup_backend.py'])
print(f"\n[RESULT 1] Exit code: {result1.returncode}\n")

print("=" * 50)
print("Running create_dirs.py...")
print("=" * 50)
result2 = subprocess.run([sys.executable, 'create_dirs.py'])
print(f"\n[RESULT 2] Exit code: {result2.returncode}\n")

if os.path.exists('create_dirs.js'):
    print("=" * 50)
    print("Running create_dirs.js...")
    print("=" * 50)
    result3 = subprocess.run(['node', 'create_dirs.js'])
    print(f"\n[RESULT 3] Exit code: {result3.returncode}\n")
else:
    print("create_dirs.js not found, skipping...")

print("\n" + "=" * 50)
print("LISTING BACKEND STRUCTURE")
print("=" * 50)
backend_path = r'C:\Users\DELL\Documents\projet\immo\backend'
if os.path.exists(backend_path):
    for root, dirs, files in os.walk(backend_path):
        level = root.replace(backend_path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
else:
    print(f"Backend directory not found: {backend_path}")

print("\n" + "=" * 50)
print("LISTING FRONTEND STRUCTURE")
print("=" * 50)
frontend_path = r'C:\Users\DELL\Documents\projet\immo\frontend'
if os.path.exists(frontend_path):
    for root, dirs, files in os.walk(frontend_path):
        level = root.replace(frontend_path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
else:
    print(f"Frontend directory not found: {frontend_path}")
