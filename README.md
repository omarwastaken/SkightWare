# SkightWare
## A Keylogger and Reverse Shell Made For Windows.

### Features:
- Has a PowerShell reverse shell.
- Able to log keys pressed (Obviously).
- Detects Uppercase and Lowercase based on: Caps-Lock, Shift, R-Shift.
- Logs current window being viewed.
- Exits when the user pressed ESC (You can remove it yourself but I'm not responsible of how you use it.

### To use this tool you need to do the following:
1. Install requirments:
```bash
pip install requirements
```
2. Edit IP and Port in the code.
3. Install Pyinstaller:
```bash
pip install pyinstaller
```
4. Build the tool using Pyinstaller:
```bash
pyinstaller --onefile --noconsole my_script.py
```

You'll find the exe in the "dist" folder.

# DISCLAIMER
### This tool is intended for educational purposes only. Please be aware that using it for any illegal activity is strictly prohibited and at your own risk. I take no responsibility for any misuse of this project.
