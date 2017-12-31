import PIL.ImageGrab
import os
import time
import win32gui
import sys

def screenGrab():

    #get the duellinks window (location and size)
    hwnd = win32gui.FindWindow(0,"Yu-Gi-Oh! DUEL LINKS")
    if not hwnd:
        print("Yu-Gi-Oh! DUEL LINKS is not open on your computer. Open it and try again!")
        sys.exit()
    else:
        print("in here")
        win32gui.ShowWindow(hwnd,1)
        win32gui.BringWindowToTop(hwnd)
        rect = win32gui.GetWindowRect(hwnd)
        window_x = rect[0]
        window_y = rect[1]
        window_width = rect[2] - window_x
        window_height = rect[3] - window_y
        box = (rect[0],rect[1],rect[2],rect[3])
        im = PIL.ImageGrab.grab(box)
        im.save(os.getcwd() + '\\data\\screenshots\\img_' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
