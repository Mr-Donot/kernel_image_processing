from PIL import Image



def get_pixel_value(initial_pixels, kernel) -> [int, int, int]:
    result = [0,0,0]
    for i in range(len(kernel)):
        for j in range(len(kernel[i])):
            for color in range(len(result)):
                result[color] += initial_pixels[i][j][color] * kernel[i][j]
    return result



def process_image(img: Image, kernel) -> Image:
    (largeur,hauteur)=img.size
    newImg = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (largeur):
        for j in range (hauteur):
            initial_pixels = []
            for k in range(len(kernel)):
                pixel_line = []
                for l in range(len(kernel[k])):
                    pos_i = i-1+l if 0 <= i-1+l < largeur else i
                    pos_j = j-1+k if 0 <= j-1+k < hauteur else j
                    pixel_line.append(img.getpixel((pos_i, pos_j)))

                initial_pixels.append(pixel_line)

            new_value = get_pixel_value(initial_pixels, kernel)
            newImg.putpixel((i,j), tuple(new_value))
    newImg.show()
    return newImg