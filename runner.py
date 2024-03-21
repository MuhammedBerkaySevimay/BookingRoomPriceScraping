import subprocess
import os
import sys

application_path = os.path.dirname(sys.executable)

script = f"""
tell application "Terminal"
    do script "cd '{application_path}' && './marius'"
end tell
"""

subprocess.run(["osascript", "-e", script], check=True)
