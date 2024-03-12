import subprocess
import os
import sys

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

script = f"""
tell application "Terminal"
    do script "cd '{application_path}' && './marius'"
end tell
"""

subprocess.run(["osascript", "-e", script], check=True)
