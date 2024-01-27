from PIL import Image
from utils import *
import multiprocessing

def process_strip(img, kernel, start_row, end_row):
    (width, height) = img.size
    strip = Image.new('RGB', (width, end_row - start_row), color=(0, 0, 0))
    for i in range(width):
        for j in range(start_row, end_row):
            initial_pixels = []
            for k in range(len(kernel)):
                pixel_line = []
                for l in range(len(kernel[k])):
                    pos_i = i - 1 + l if 0 <= i - 1 + l < width else i
                    pos_j = j - 1 + k if 0 <= j - 1 + k < height else j
                    pixel_line.append(img.getpixel((pos_i, pos_j)))

                initial_pixels.append(pixel_line)

            new_value = get_pixel_value(initial_pixels, kernel)
            strip.putpixel((i, j - start_row), tuple(new_value))

    return start_row, end_row, strip

def process_image_parallel(img: Image, kernel, num_processes) -> Image:
    (width, height) = img.size
    strip_height = height // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = []
        for i in range(0, height, strip_height):
            end_row = min(i + strip_height, height)
            results.append(
                pool.apply_async(process_strip, (img, kernel, i, end_row))
            )

        new_img = Image.new('RGB', (width, height), color=(0, 0, 0))
        for result in results:
            start_row, end_row, strip = result.get()
            new_img.paste(strip, (0, start_row))

    return new_img