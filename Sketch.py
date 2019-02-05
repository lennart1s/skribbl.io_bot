import Mouse, Skribbler

import requests
from PIL import Image
from io import BytesIO

def getRGBAFrom(url, sketchWidth, sketchHeight):
    result = requests.get(url)
    img = Image.open(BytesIO(result.content))

    xFac = sketchWidth / img.width
    yFac = sketchHeight / img.height
    print(xFac, yFac)
    fac = 0
    if xFac < yFac:
        fac = xFac
    else:
        fac = yFac
    Skribbler.width = int(img.width*fac)
    Skribbler.height = int(img.height*fac)
    img = img.resize((Skribbler.width, Skribbler.height))

    print(Skribbler.width, Skribbler.height)

    rgba = img.convert("RGBA")

    return rgba