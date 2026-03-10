#!/usr/bin/env python3
"""Helper script to run all setup scripts."""
import os
import subprocess
import sys

base = r'C:\Users\DELL\Documents\projet\immo'

print("=" * 60)
print("Running setup_backend.py...")
print("=" * 60)
try:
    result = subprocess.run(
        [sys.executable, os.path.join(base, 'setup_backend.py')],
        cwd=base,
        capture_output=True,
        text=True,
        timeout=30
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    print("Return code:", result.returncode)
except Exception as e:
    print('Error running setup_backend.py:', e)
    sys.exit(1)

print("\n" + "=" * 60)
print("Running create_dirs.py...")
print("=" * 60)
try:
    result2 = subprocess.run(
        [sys.executable, os.path.join(base, 'create_dirs.py')],
        cwd=base,
        capture_output=True,
        text=True,
        timeout=30
    )
    print(result2.stdout)
    if result2.stderr:
        print("STDERR:", result2.stderr)
    print("Return code:", result2.returncode)
except Exception as e:
    print('Error running create_dirs.py:', e)
    sys.exit(1)

print("\n" + "=" * 60)
print("Running create_dirs.js...")
print("=" * 60)
try:
    result3 = subprocess.run(
        ['node', os.path.join(base, 'create_dirs.js')],
        cwd=base,
        capture_output=True,
        text=True,
        timeout=30
    )
    print(result3.stdout)
    if result3.stderr:
        print("STDERR:", result3.stderr)
    print("Return code:", result3.returncode)
except Exception as e:
    print('Error running create_dirs.js:', e)
    sys.exit(1)

print("\n" + "=" * 60)
print("All scripts completed!")
print("=" * 60)
