import Mouse

import requests
from PIL import Image
from io import BytesIO

def getRGBAFrom(url, sketchWidth, sketchHeight):
    result = requests.get(url)
    img = Image.open(BytesIO(result.content))
    img = img.resize((sketchWidth, sketchHeight))
    rgba = img.convert("RGBA")

    return rgba