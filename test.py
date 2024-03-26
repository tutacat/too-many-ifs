import subprocess
import sys

sys.argv += ("0",)
print('even' if subprocess.run(("./iseven_o.py",sys.argv[1])).returncode==0 else 'odd')
