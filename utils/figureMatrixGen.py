from PIL import Image
import numpy as np


def compressTo(im, resize_ratio=0.5):
    w, h = np.dot(im.size, resize_ratio).astype(int)
    return im.resize((w, h), Image.ANTIALIAS)

def figureMatrixGen(pixelArr):
    # 1020 -> white
    return (pixelArr != 1020).astype(int)

def matrixToFile(arr):
    w, h = arr.shape
    with open('res.matrix', 'w') as f:
        for i in range(w):
            for j in range(h):
                f.write(str(arr[i][j]) + ' ')
            f.write('\n')

def getFigure(imgSrc):
    with Image.open(imgSrc) as im:
        im_compressed = compressTo(im, 0.3)
        pixelArr = np.sum(np.array(im_compressed), 2)
        figureMatrix = figureMatrixGen(pixelArr)

    return figureMatrix


if __name__ == '__main__':
    pass
