import cv2
import numpy as np
from tqdm import tqdm

spectrum_dog = cv2.imread('Spectrum/dog.png')
spectrum_human = cv2.imread('Spectrum/human.png')
stock = cv2.imread('stock_compr.jpg')

out_img = np.zeros(stock.shape, np.uint8)

def MakeMatrix (img) :
    out_arr = np.zeros((3, 1000), dtype=int)
    cur_color = []

    if img.shape[0] == 100 and img.shape[1] == 1000:
        for i in range(1000):
            for j in range(3):
                for l in range(100):
                    cur_color.append(img[l, i, j])
                out_arr[j][i] = int(np.mean(cur_color))
                cur_color.clear()

    return out_arr

dog_arr = MakeMatrix(spectrum_dog)
human_arr = MakeMatrix(spectrum_human)

coord = 0

for i in tqdm(range(stock.shape[0])):
    for j in range(stock.shape[1]):
        for l in range(1000):
            if int(stock[i][j][0]) == human_arr[0][l] and int(stock[i][j][1]) == human_arr[1][l] and int(stock[i][j][2]) == human_arr[2][l]:
                coord = l
                break
        out_img[i][j] = (dog_arr[0][coord], dog_arr[1][coord], dog_arr[2][coord])

cv2.imwrite('output_img.png', out_img)