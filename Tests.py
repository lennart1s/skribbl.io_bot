import win32con, win32api, requests
from PIL import Image
from io import BytesIO

def cursTo(x, y):
    win32api.SetCursorPos((x, y))

def click(x, y): 
    cursTo(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) 

#print(win32api.GetCursorPos())
#click(30, 50)

try:
    res = requests.get("https://image.airbrush-city.de/item/images/202489/full/Flex-T-Shirt-Textil-Plotter-Folie-DIN-A4-Neon-Blau.jpg")
    img = Image.open(BytesIO(res.content))
    #img = img.resize((10, 10))
    #img.save("newimg.jpg")
    rgb = img.convert("RGB")
    r, g, b = rgb.getpixel((0,0))
    print(r,g,b)
    width, height = img.size
    print(width, height)
except IOError:
    pass