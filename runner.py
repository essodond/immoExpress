import subprocess
import sys

try:
    result = subprocess.run([sys.executable, r'C:\Users\DELL\Documents\projet\immo\final_setup.py'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    sys.exit(result.returncode)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
