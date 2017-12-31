import win32gui
class window:
    hwnd = win32gui.FindWindow(0,"Yu-Gi-Oh! DUEL LINKS")
    if not hwnd:
        print("ERROR! DUEL LINKS IS NOT OPEN!")
    else:
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        width = rect[2] - x
        height = rect[3] - y
                    

