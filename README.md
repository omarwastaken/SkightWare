# SkightWare
## A Keylogger and Reverse Shell Made For Windows.

---

### Project Overview:
SkightWare is a tool designed for educational and ethical purposes, combining keylogging and reverse shell capabilities for Windows environments. This project demonstrates a deep understanding of both offensive security techniques and defensive programming practices.

### Technical Details:

1. **Reverse Shell:**
   - **Implementation:** Utilises PowerShell to establish a reverse shell connection.
   - **Connectivity:** Continuously attempts to connect to a specified IP and port, allowing remote command execution.
   - **Data Transfer:** Bi-directional communication is achieved through socket programming, seamlessly sending data between the server and the client.

2. **Keylogger:**
   - **Key Press Logging:** Captures all keystrokes, intelligently distinguishing between uppercase and lowercase letters based on Caps Lock and Shift key states.
   - **Active Window Tracking:** Logs the title of the active window, providing context to the captured keystrokes.
   - **Clipboard Monitoring:** Monitors and logs clipboard content changes, ensuring comprehensive data capture.
   - **Data Storage:** All captured data is saved in a `log.txt` file for later analysis.

3. **Safety and Ethical Considerations:**
   - **Transparency:** The project includes features that make it visible and easily terminable, reinforcing its educational purpose.
   - **Exit Mechanism:** Users can terminate the keylogger by pressing the ESC key, ensuring that the tool can be easily disabled.

### Features:
- **PowerShell Reverse Shell:** Facilitates remote command execution and system control.
- **Keystroke Logging:** Captures detailed keypress data, considering Caps Lock and Shift key states.
- **Window Activity Logging:** Records the title of the active window to provide context for keystrokes.
- **Clipboard Content Monitoring:** Tracks changes in clipboard content.
- **Comprehensive Logging:** All activities are logged in a readable format in `log.txt`.
- **Easy Termination:** The keylogger can be easily stopped by pressing the ESC key.

---

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

---

##   Sponsor this project
<a href='https://ko-fi.com/skight' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />

# DISCLAIMER
### This tool is intended for ethical purposes only. Please be aware that using it for any illegal activity is strictly prohibited and at your own risk. I take no responsibility for any misuse of this project.
