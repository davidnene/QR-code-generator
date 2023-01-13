#!/usr/bin/python3
"""
We will use this file to test the program
""" 

#import the function from QR.py
qr_generator = __import__('QR').qr_generator

#intilialize input to capture and save the data in the CLI into a variable
link = input("Enter link to generate QR code:")
title = input("Enter link title here:")

#initialize the function
qr_generator(link, title)
