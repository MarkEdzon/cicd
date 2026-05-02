import os
import sys

if os.path.exists("index.php"):
    print("Test Passed")
    sys.exit(0)
else:
    print("Test Failed")
    sys.exit(1)
