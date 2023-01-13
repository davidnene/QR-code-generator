#!/usr/bin/python3
import pyqrcode
import png
from PIL import Image


def qr_generator(link, title):
    qr_code = pyqrcode.create(link)
    qr_code.png(f"{title}.png", scale=5)
    im = Image.open(f"{title}.png")
    im.show()
