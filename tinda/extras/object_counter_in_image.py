import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

def object_counter_in_image(image_file):
    image = cv2.imread(image_file)
    box, label, count = cv.detect_common_objects(image)
    output = draw_bbox(image, box, label, count)
    plt.imshow(output)
    plt.show()
    print(f"Number if objects in the image are '{str(label.count('object'))}'")


object_counter_in_image('cars.jpeg')

