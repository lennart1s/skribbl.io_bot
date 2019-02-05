import Mouse

import requests
from PIL import Image
from io import BytesIO

def getRGBFrom(url, sketchWidth, sketchHeight):
    result = requests.get(url)
    img = Image.open(BytesIO(result.content))
    img = img.resize((sketchWidth, sketchHeight))
    rgb = img.convert("RGB")

    return rgb