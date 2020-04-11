#!/usr/bin/python
import os
import sys
import time
from time import sleep as out
import subprocess
def bersih():
    os.system("clear")
def kembali():
    ye = input("Did you subscrifbed? (y/n): ")
    if ye == "y":
       subprocess.call("python virus.py",shell=True)
    elif ye == "n":
         print ("Go and subsribe")
         time.sleep(1)
         os.system("exit")
    else:
         print ("TThank you!!!")
         time.sleep(1)
         kembali()

#clear
