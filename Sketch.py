import Mouse

import requests
from PIL import Image
from io import BytesIO

sketchWidth = 0
sketchHeight = 0

def getRGBAFrom(url, canvasWidth, canvasHeight):
    global sketchWidth, sketchHeight
    
    result = requests.get(url)
    img = Image.open(BytesIO(result.content))

    xFac = canvasWidth / img.width
    yFac = canvasHeight / img.height
    fac = 0
    if xFac < yFac:
        fac = xFac
    else:
        fac = yFac
    sketchWidth = int(img.width*fac)
    sketchHeight = int(img.height*fac)
    print(sketchWidth, sketchHeight)
    img = img.resize((sketchWidth, sketchHeight))

    rgba = img.convert("RGBA")

    return rgba