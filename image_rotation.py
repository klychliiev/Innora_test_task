from angle_detection import calculate_angle
from PIL import Image
import os
import random
from natsort import natsorted

INPUT_IMAGES_PATH = 'invoices_rotated'
ROTATED_IMAGES_PATH = 'rotated_images'


def rotate_image(input_images, rotated_images):

    for image in natsorted(os.listdir(input_images)):
        image_path = os.path.join(input_images, image)
        detected_angle = calculate_angle(image_path)
        pil_image = Image.open(image_path)

        if detected_angle in range(-30,31):
            rotated_image = pil_image.rotate(detected_angle)
            rotated_image.save(f'{rotated_images}/{image}')
        else:
            continue


if __name__ == '__main__':
    rotate_image(INPUT_IMAGES_PATH,
                ROTATED_IMAGES_PATH)
