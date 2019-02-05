import Mouse

topLeft = (500, 260)
bottomRight = (1280, 850)
width = 780
height = 590

lastColorKey = ""

btns = {"size1":(1035, 890), "size2":(1085,890), "size3":(1135, 890), "size4":(1158, 890),
    "pen":(870, 890), "eraser":(920, 890), "fill":(970, 890),
    "delete":(1240, 890),
    "white":(585, 880),"black":(585, 904),"gray":(610, 880), "red":(635, 880),"orange":(658, 880),"yellow":(680, 880),"green":(705, 880),
    "blue":(730, 880),"ocean":(755, 880),"magenta":(777, 880),"pink":(802, 880),"brown":(825, 880),}

colors = {"white": (255, 255, 255), "black": (0, 0, 0), "gray": (193, 193, 193), "red": (239, 19, 11), "orange": (255, 113, 0),
    "yellow": (255, 228, 0), "green": (0, 204, 0), "blue": (0, 178, 255), "ocean": (35, 31, 211), "magenta": (163, 0, 186), 
    "pink": (211, 124, 170), "brown": (160, 82, 45)}


def getColor(r, g, b):
    bestKey = ""
    bestDiff = 1000
    for key in colors: 
        diff = abs(colors[key][0]-r)
        diff += abs(colors[key][1]-g)
        diff += abs(colors[key][2]-b)
        if diff < bestDiff:
            bestDiff = diff
            bestKey = key
    return bestKey

def chooseColor(r, g, b):
    global lastColorKey
    
    bestKey = getColor(r, g, b)
    if bestKey != lastColorKey:
        Mouse.click(btns[bestKey])
        lastColorKey = bestKey

#def draw(rgba):
#    Mouse.click(btns["delete"])
#    Mouse.click(btns["size2"])
#
#    for x in range(0, width, 10):
#        for y in range(0, height, 10):
#            r, g, b, a = rgba.getpixel((x, y))
#            if a != 0:
#                chooseColor(r, g, b)
#                Mouse.click((topLeft[0]+x, topLeft[1]+y))
#    return

def drawPreprocessed(pixels):
    Mouse.click(btns["delete"])
    Mouse.click(btns["pen"])
    Mouse.click(btns["size2"])

    for color in pixels:
        Mouse.click(btns[color])
        for pixel in pixels[color]:
            Mouse.click((topLeft[0]+pixel[0], topLeft[1]+pixel[1]))
    print("Finished drawing!")

def preProcess(rgba):
    global colors
    
    pixels = {}
    for key in colors:
        pixels[key] = []

    for x in range(0, width, 10):
        for y in range(0, height, 10):
            r, g, b, a = rgba.getpixel((x, y))
            if a != 0:
                color = getColor(r, g, b)
                if color != "white":
                    pixels[color].append((x, y))
        
    return pixels 