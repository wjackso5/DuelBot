import PIL.ImageGrab, PIL.ImageOps
import os
import time
import win32gui, win32api, win32con
import sys
import cord
from numpy import *
#do this first
coordinates = cord.Cord
hwnd = win32gui.FindWindow(0,"Yu-Gi-Oh! DUEL LINKS")
if not hwnd:
        print("Yu-Gi-Oh! DUEL LINKS is not open on your computer. Open it and try again!")
        sys.exit()
else:
        rect = win32gui.GetWindowRect(hwnd)
        window_x = rect[0]
        window_y = rect[1]
        window_width = rect[2] - window_x
        window_height = rect[3] - window_y
        
#left mouse click
def leftClick(hold_time=0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(hold_time)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#sets the mouse position
def setMousePos(cord):
    rect = win32gui.GetWindowRect(hwnd)
    window_x = rect[0]
    window_y = rect[1]
    window_width = rect[2] - window_x
    window_height = rect[3] - window_y
    win32api.SetCursorPos((window_x + cord[0], window_y + cord[1]))

#gets the mouse position
def getMousePos():
    rect = win32gui.GetWindowRect(hwnd)
    window_x = rect[0]
    window_y = rect[1]
    window_width = rect[2] - window_x
    window_height = rect[3] - window_y
    x,y = win32api.GetCursorPos()
    x = x - window_x
    y = y - window_y
    print(x,y)
#clicks 'Initiate Link'
def initiateLink():
    setMousePos(cord.b_init)
#takes a screenshot of the DL window                          
def screenGrab():
    hwnd = win32gui.FindWindow(0,"Yu-Gi-Oh! DUEL LINKS")
    if not hwnd:
        print("Yu-Gi-Oh! DUEL LINKS is not open on your computer. Open it and try again!")
        sys.exit()
    else:
        print("taking screen capture of DUEL LINKS")
        win32gui.ShowWindow(hwnd,1)
        win32gui.BringWindowToTop(hwnd)
        rect = win32gui.GetWindowRect(hwnd)
        window_x = rect[0]
        window_y = rect[1]
        window_width = rect[2] - window_x
        window_height = rect[3] - window_y
        box = (rect[0]+1,rect[1]+1,rect[2],rect[3])
        time.sleep(.1)
        im = PIL.ImageGrab.grab(box)
        time.sleep(.1)
        win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
        return im
#compares a screen cap to an already taken image to see if we are in the state to proceed
#takes in the image and the expected value for the image and then how different they can be for the method to return true
#use mean square error
def compare_im(im, ev_im, acceptable_err):
    err = sum((im.astype("float") - ev_im.astype("float")) ** 2)
    err /= float(im.shape[0] * ev_im.shape[1])
    if (err<acceptable_err):
        return true
                
    else:
        return false
        
def main():
    pass

if __name__ == '__main__':
    main()
