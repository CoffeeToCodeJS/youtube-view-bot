import os
import sys
import time

class Software:
    name = "YouTube View Bot"
    ver = 1

os.system("cls")
print "-| Welcome to the " + Software.name + ". Please enter a video URL. |-"
print ""
url = raw_input("url:  ")

def openURL():
    os.system("start " + url)
    time.sleep(3)
    openURL()

openURL()
