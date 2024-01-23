from PIL import Image


from utils import *

kernel_sharpen = [
    [0, -1, 0], 
    [-1, 5, -1], 
    [0, -1, 0]
]

kernel_ridge = [
    [-1, -1, -1], 
    [-1, 8, -1], 
    [-1, -1, -1]
]

kernel_identity = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

img1 = Image.open("img/wiki_example.png")

img2 = process_image(img1, kernel_ridge)

