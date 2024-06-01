# THIS PROJECT IS FOR EDUCATIONAL PURPOSES ONLY

# Keylogger
![developers](https://img.shields.io/badge/Developed%20By:-Furman%20Vlad-red)

Keystroke Logging to capture all keyboard input and Screen Capture for periodic screenshots of user activity. It operates in Stealth Mode, running undetected and hidden from the task manager and system tray. Additionally, it provides Email Reporting, sending log files and screenshots to a specified email address at configurable intervals for regular updates.

## Features

1. **Keystroke Logging**
   - Captures all keystrokes entered on the keyboard.

2. **Screen Capture**
   - Takes periodic screenshots to visually monitor user activity.
   - Configurable interval for taking screenshots.

3. **Stealth Mode**
   - Runs in the background without being detected.
   - Hides from task manager and system tray.

4. **Email Reporting**
   - Sends log files and screenshots to a specified email address.
   - Configurable email sending intervals.


## How To Run This Project
- Download Keylogger.py
- Open a command prompt or terminal
- Navigate to the directory where your script is located
- Run following command:
```
pip install -r requirements.txt
```
- Change these fields in the code:
```
SENDER_EMAIL = 'example@example.com'
RECEIVER_EMAIL = 'example@example.com'
SMTP_SERVER = 'smtp.example.com' ('smtp.office365.com')
SMTP_PORT = 587
USERNAME = 'example@example.com' (Same as SENDER_EMAIL)
PASSWORD = '*********'
```
- To make convert the .py script to .exe:
- Navigate to the directory where your script is located (cd Desktop) and write:
```
pyinstaller --onefile --noconsole your_script_name.py
```
- You can find the executable file in the dist directory within your script's directory.
- The file will have the same name as your_script_name

## Video
- https://youtu.be/wRjUAHPQq6E
