#!/usr/bin/python3
import pyqrcode
import png
from PIL import Image


link = input("Enter link to generate QR code:")
title = input("Enter link title here:")

def qr_generator(link, title):
    qr_code = pyqrcode.create(link)
    qr_code.png(f"{title}.png", scale=5)
    Image.open(f"{title}.png")