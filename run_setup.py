import subprocess
import os

# Run the Node.js script
result = subprocess.run(
    ['node.exe', r'C:\Users\DELL\Documents\projet\immo\master_setup.js'],
    capture_output=True, text=True, cwd=r'C:\Users\DELL\Documents\projet\immo'
)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)

# Check if files exist
print("\n" + "="*60)
print("FILE EXISTENCE CHECK:")
print("="*60)

files_to_check = [
    r'C:\Users\DELL\Documents\projet\immo\backend\src\server.js',
    r'C:\Users\DELL\Documents\projet\immo\backend\package.json',
    r'C:\Users\DELL\Documents\projet\immo\frontend\src\app\catalogue\.gitkeep'
]

for file_path in files_to_check:
    exists = os.path.exists(file_path)
    print(f"{file_path}")
    print(f"  Exists: {exists}")
