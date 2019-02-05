import Mouse, Sketch

import requests, time
from PIL import Image
from io import BytesIO

rgb = None

def countdown(t):
    for i in range(0, t):
        print(t-i, end=' ')
        time.sleep(1)
    print()

def init():
    print("Move cursor to top left corner of canvas!")
    countdown(1)
    canvasTopLeft = Mouse.getPosition()
    print("Top-Left corner:", canvasTopLeft)

    print("Move cursor to bottom right corner of canvas!")
    countdown(1)
    Sketch.bottomRight = Mouse.getPosition()
    print("Bottom-Right corner:", Sketch.bottomRight)

    Sketch.width = Sketch.bottomRight[0] - Sketch.topLeft[0]
    Sketch.height = Sketch.bottomRight[1] - Sketch.topLeft[1]
    print("Canvas-Dimensions:", Sketch.width, Sketch.height)

def loadURL(url):
    global rgb
    if Sketch.width == 0 or Sketch.height == 0:
        print("Canvas is not initialized! Try running 'init'")
        return
    rgb = Sketch.getRGBFrom(cmd.replace("url ", ""), Sketch.width, Sketch.height)
    print("Loaded image successfully!")

cmd = input()
while cmd != "exit":
    if cmd == "init":
        init()
    elif cmd.startswith("url "):
        loadURL(cmd.replace("url ", ""))
    elif cmd == "draw":
        Sketch.draw(rgb)
    else:
        print("Unknown command!")
    cmd = input()