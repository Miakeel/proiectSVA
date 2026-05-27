import numpy as np
import cv2

def is_foreign_symbol(img) -> bool:
    
    h, w = img.shape[:2]

    img = img[int(h*0.2):int(h*0.8),int(w*0.2):int(w*0.8)]

    kernel = np.ones((3,3), np.uint8)

    thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=2)

    thresh = cv2.dilate(thresh,kernel,iterations=2)

    density = np.sum(img > 0) / img.size

    if density > 0.1:
        return True

    return False