from angle_detection import calculate_angle
from PIL import Image
import os
import random

INPUT_IMAGES_PATH = 'invoices_rotated'
ROTATED_IMAGES_PATH = 'rotated_images'


def rotate_image(input_images, rotated_images):

    for image in os.listdir(input_images):

        image_path = os.path.join(input_images, image)

        detected_angle = calculate_angle(image_path)

        pil_image = Image.open(image_path)

        rotated_image = pil_image.rotate(detected_angle)

        rotated_image.save(f'{rotated_images}/{image}')


if __name__ == '__main__':
    rotate_random_image(INPUT_IMAGES_PATH,
                        ROTATED_IMAGES_PATH)
