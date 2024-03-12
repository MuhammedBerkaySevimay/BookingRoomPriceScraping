For building this project you must use pyinstaller.

"runner.py" file is open a terminal in OSX and run compiled file "marius" in the same directory.

You must compile "marius.py" and "runner.py" and copy "token.txt" file to "dist" directory. Then rename "runner" to "runner.app". Now you able to use by double clicking on it.

You can use "pyinstaller -F marius.py" and "pyinstaller -F runner.py" for compile files.
