import numpy as np
from PIL import Image, ImageDraw
import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# print(width, height)

im = Image.new('RGB', size=(width, height), color='black')
