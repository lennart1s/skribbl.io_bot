import Mouse

import requests
from PIL import Image
from io import BytesIO

topLeft = (500, 260)
bottomRight = (1280, 850)
width = 780
height = 590

btns = {"size1":(1035, 890), "size2":(1085,890), "size3":(1135, 890), "size4":(1158, 890),
    "pen":(870, 890), "eraser":(920, 890), "fill":(970, 890),
    "delete":(1240, 890),
    "white":(585, 880),"black":(585, 904),"gray":(610, 880), "red":(635, 880),"orange":(658, 880),"yellow":(680, 880),"green":(705, 880),
    "blue":(730, 880),"ocean":(755, 880),"magenta":(777, 880),"pink":(802, 880),"brown":(825, 880),}

def getRGBFrom(url, sketchWidth, sketchHeight):
    result = requests.get(url)
    img = Image.open(BytesIO(result.content))
    img = img.resize((sketchWidth, sketchHeight))
    rgb = img.convert("RGB")

    return rgb

def draw(rgb):
    Mouse.click(btns["delete"])
    Mouse.click(btns["size2"])

    Mouse.click(btns["black"])
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = rgb.getpixel((x, y))
            if (r+g+b)/3 > 255/2 :
                Mouse.click((topLeft[0]+x, topLeft[1]+y))
    return