import Mouse, Sketch, Skribbler

import requests, time
from PIL import Image
from io import BytesIO

rgba = None
preProcessed = None

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
    Skribbler.bottomRight = Skribbler.getPosition()
    print("Bottom-Right corner:", Sketch.bottomRight)

    Skribbler.width = Skribbler.bottomRight[0] - Skribbler.topLeft[0]
    Skribbler.height = Skribbler.bottomRight[1] - Skribbler.topLeft[1]
    print("Canvas-Dimensions:", Skribbler.width, Skribbler.height)

def loadURL(url):
    global rgba
    if Skribbler.width == 0 or Skribbler.height == 0:
        print("Canvas is not initialized! Try running 'init'")
        return
    rgba = Sketch.getRGBAFrom(cmd.replace("url ", ""), Skribbler.width, Skribbler.height)
    print("Loaded image successfully!")

def preProcess():
    global preProcessed, rgba

    preProcessed = Skribbler.preProcess(rgba)
    print("Preprocessed image!")

cmd = input()
while cmd != "exit":
    if cmd == "init":
        init()
    elif cmd.startswith("url "):
        loadURL(cmd.replace("url ", ""))
        preProcess()
    elif cmd == "draw":
        Skribbler.drawPreprocessed(preProcessed)
    #elif cmd == "drawPre":
        #Skribbler.drawPreprocessed(preProcessed)
    else:
        print("Unknown command!")
    cmd = input()