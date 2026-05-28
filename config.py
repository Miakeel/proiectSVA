IMAGE_PATH = "testing_photos/tttfail2.jpeg"  # change photo name to select photo to use
BOARD_SIZE = 500
LINE_THRESHOLD = 20
IS_PHOTO_REAL = 1

O_CLOSING_KERNEL_SIZE = 5
O_CLOSING_ITERATIONS = 2

FOREIGN_MARGIN = 0.20        # fraction of cell edge cropped to remove grid lines
FOREIGN_MIN_DENSITY = 0.02   # minimum foreground pixel ratio to consider cell non-empty
FOREIGN_MIN_CONTOUR_AREA = 10  # minimum contour area (px²) to count as a real mark