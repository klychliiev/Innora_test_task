from angle_detection import calculate_angle
from PIL import Image
import os
import random

PATH = 'invoices_rotated'


def rotate_random_image(path):

    random_file = random.choice(os.listdir(path))

    image_path = os.path.join(path, random_file)

    detected_angle = calculate_angle(image_path)

    pil_image = Image.open(image_path)

    rotated_image = pil_image.rotate(detected_angle)

    rotated_image.show()


if __name__ == '__main__':
    rotate_random_image(PATH)
