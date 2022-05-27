This script will record keystrokes on a target machine and email the results to a specified gmail account with a specified time interval.  For example, you can configure it to record key strokes on a computer and email the results to you every 15 minutes.

Open up run_keylogger.py to create an instance of the key_logger class.  Enter in A, B, C (see below) then run run_keylogger.py in terminal to begin logging keystrokes on that machine.  

Enter in the following for keylogger.Keylogger(A, "B", "C")

A = how many second intervals you want to log keystrokes and email them out
B = receiving gmail of the key log (this only works with gmail)
C = password of gmail account

These scripts can be turned into an executable or run on any machine that has a Python intepretor.

