#!/usr/bin/python3

qr_generator = __import__('QR').qr_generator

link = input("Enter link to generate QR code:")
title = input("Enter link title here:")

qr_generator(link, title)
