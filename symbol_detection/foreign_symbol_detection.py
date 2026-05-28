import cv2
import numpy as np

from config import FOREIGN_MARGIN, FOREIGN_MIN_DENSITY, FOREIGN_MIN_CONTOUR_AREA


def _to_binary_foreground(image: np.ndarray) -> np.ndarray:
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # Ensure foreground is white
    if np.count_nonzero(binary) > binary.size // 2:
        binary = cv2.bitwise_not(binary)
    return binary


def detect_foreign(
    image: np.ndarray,
    margin: float = FOREIGN_MARGIN,
    min_density: float = FOREIGN_MIN_DENSITY,
    min_contour_area: int = FOREIGN_MIN_CONTOUR_AREA,
) -> bool:
    binary = _to_binary_foreground(image)

    # Crop cell borders to exclude grid line remnants
    h, w = binary.shape
    binary = binary[
        int(margin * h) : int((1 - margin) * h),
        int(margin * w) : int((1 - margin) * w),
    ]

    # Reject cells with negligible ink (likely empty)
    if np.count_nonzero(binary) / binary.size < min_density:
        return False

    # Confirm structured content via at least one contour of meaningful size
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return any(cv2.contourArea(c) >= min_contour_area for c in contours)
