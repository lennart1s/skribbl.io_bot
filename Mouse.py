import win32con, win32api

def click(x, y): 
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) 

def getPosition():
    return win32api.GetCursorPos()