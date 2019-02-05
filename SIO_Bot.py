import Mouse, Sketch

import requests, time
from PIL import Image
from io import BytesIO

canvasTopLeft = (0, 0)
canvasBottomRight = (0, 0)
sketchWidth = 0
sketchHeight = 0

rgb = None

def countdown(t):
    for i in range(0, t):
        print(t-i, end=' ')
        time.sleep(1)
    print()

def init():
    global canvasTopLeft
    global canvasBottomRight
    global sketchWidth
    global sketchHeight

    print("Move cursor to top left corner of canvas!")
    countdown(1)
    canvasTopLeft = Mouse.getPosition()
    print("Top-Left corner:", canvasTopLeft)

    print("Move cursor to bottom right corner of canvas!")
    countdown(1)
    canvasBottomRight = Mouse.getPosition()
    print("Bottom-Right corner:", canvasBottomRight)

    sketchWidth = canvasBottomRight[0] - canvasTopLeft[0]
    sketchHeight = canvasBottomRight[1] - canvasTopLeft[1]
    print("Canvas-Dimensions:",sketchWidth,sketchHeight)

def loadURL(url):
    global sketchWidth
    global sketchHeight
    if sketchWidth == 0 or sketchHeight == 0:
        print("Canvas is not initialized! Try running 'init'")
        return
    rgb = Sketch.getRGBFrom(cmd.replace("url ", ""), sketchWidth, sketchHeight)
    print("Loaded image successfully!")

cmd = input()
while cmd != "exit":
    if cmd == "init":
        init()
    elif cmd.startswith("url "):
        loadURL(cmd.replace("url ", ""))
    else:
        print("Unknown command!")
    cmd = input()