import os
import sys

# Check if index.php exists
if not os.path.exists("index.php"):
    print("FAIL: index.php not found")
    sys.exit(1)

# Read file content
with open("index.php", "r") as file:
    content = file.read()

# Basic validation
if "hello world" in content.lower():
    print("PASS: index.php contains expected content")
    sys.exit(0)
else:
    print("FAIL: Expected content not found")
    sys.exit(1)
