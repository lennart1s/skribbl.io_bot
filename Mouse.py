import win32con, win32api

def click(t): 
    win32api.SetCursorPos(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, t[0], t[1], 0, 0) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, t[0], t[1], 0, 0) 

def getPosition():
    return win32api.GetCursorPos()