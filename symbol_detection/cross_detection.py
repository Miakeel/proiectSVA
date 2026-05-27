import cv2
import numpy as np

def is_cross(binary_img):
    img = binary_img.copy()

    img = img.astype(np.uint8)

    k45 = np.array([[-1,0,1],[0,1,0],[1,0,-1]], np.float32)
    k135 = np.array([[1,0,-1],[0,1,0],[-1,0,1]], np.float32)

    r45 = cv2.filter2D(img, cv2.CV_32F, k45)
    r135 = cv2.filter2D(img, cv2.CV_32F, k135)

    h, w = img.shape
    mask = np.zeros_like(img, dtype=np.uint8)

    # only center region
    mask[h//4:3*h//4, w//4:3*w//4] = 1

    e45 = np.sum(np.abs(r45) * mask)
    e135 = np.sum(np.abs(r135) * mask)

    total = np.sum(mask) + 1e-6

    e45 /= total
    e135 /= total

    # adaptive threshold idea
    return (e45 > 8) and (e135 > 8)