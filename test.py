from PIL import Image
from matplotlib import pyplot as plt

from utils import *
from para_utils import *
from time import time


if __name__ == '__main__':
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

    imgs_path = [200]


    num_processes = 2

    seq_time = []
    par_time = []
    par_time2 = []

    for path in imgs_path:

        img = Image.open("img/" + str(path) + "x" + str(path)+ ".png")

        t0 = time()
        img2 = process_image(img, kernel_sharpen)
        t1 = time()
        img3 = process_image_parallel(img, kernel_sharpen, num_processes)
        t2 = time()
        img4 = process_image_parallel(img, kernel_sharpen, 8)
        t3 = time()
        seq_time.append(t1-t0)
        par_time.append(t2-t1)
        par_time2.append(t3-t2)
        print(path, "done")

    plt.style.use('seaborn-darkgrid')

    plt.plot(imgs_path, seq_time, color="red", label="Sequential", marker='o', linestyle='-', linewidth=2, markersize=8)
    plt.plot(imgs_path, par_time, color="blue", label="Parallel 2 cores", marker='s', linestyle='--', linewidth=2, markersize=8)
    plt.plot(imgs_path, par_time2, color="purple", label="Parallel 8 cores", marker='p', linestyle='--', linewidth=2, markersize=8)

    # Add labels to the axes
    plt.xlabel('Image', fontsize=12)
    plt.ylabel('Time', fontsize=12)

    # Add a title to the plot
    plt.title('Sequential vs Parallel Execution Times', fontsize=14)

    # Add a legend with a shadow effect
    plt.legend(fontsize=10, shadow=True)

    # Add a grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()




