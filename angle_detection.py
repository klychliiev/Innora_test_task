import numpy as np
import cv2
import math
from PIL import Image
import json
import os
from natsort import natsorted
from scipy import ndimage



PATH = 'invoices_rotated'


def calculate_angle(image_path):

    img_before = cv2.imread(image_path)

    img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0,
                            100, minLineLength=100, maxLineGap=5)

    angles = []

    for [[x1, y1, x2, y2]] in lines:
        cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        angles.append(angle)

    median_angle = np.median(angles)

    # img_rotated = ndimage.rotate(img_before, median_angle)
    # cv2.imwrite('lines_detected.jpg', img_rotated)  

    return round(median_angle, 2)


def generate_json(images_path):

    predicted_angles = {}

    for image in natsorted(os.listdir(images_path)):
        image_path = os.path.join(images_path, image)

        # the negative angle is used because we need not a rotation angle
        # but an angle-to-rotate the image to normalize it
        negative_angle = -(round(calculate_angle(image_path)))

        # detect an angle within the range of [-30,30] degrees
        if negative_angle in range(-30, 31):
            predicted_angles[image_path] = negative_angle
            print(f'{image_path}: {negative_angle}')
        else:
            continue

    with open('predicted_angles.json', 'w') as json_file:
        # store image paths as keys and predicted angles as values into a  JSON file
        json.dump(predicted_angles, json_file, indent=4)


if __name__ == '__main__':
    generate_json(PATH)
