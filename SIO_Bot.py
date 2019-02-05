import Mouse, Sketch

import requests
from PIL import Image
from io import BytesIO

Mouse.click(0, 0)
rgb = Sketch.getRGBFrom("https://image.airbrush-city.de/item/images/202489/middle/Flex-T-Shirt-Textil-Plotter-Folie-DIN-A4-Neon-Blau.jpg", 500, 500)