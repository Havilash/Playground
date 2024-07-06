import random
from PIL import Image
import requests
from enum import Enum
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np


class Direction(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


def split_image(img: Image, direction: Direction):
    width, height = img.size

    if direction == Direction.HORIZONTAL:
        img1 = img.crop((0, 0, width, height // 2))
        img2 = img.crop((0, height // 2, width, height))
    elif direction == Direction.VERTICAL:
        img1 = img.crop((0, 0, width // 2, height))
        img2 = img.crop((width // 2, 0, width, height))
    else:
        raise ValueError(
            "Direction must be either 'Direction.HORIZONTAL' or 'Direction.VERTICAL'"
        )

    return img1, img2


def get_images_url(url="https://picsum.photos/800/800?random=1"):
    response = requests.get(url)
    try:
        img = Image.open(BytesIO(response.content))
        direction = (
            Direction.HORIZONTAL if random.random() > 0.5 else Direction.VERTICAL
        )
        img1, img2 = split_image(img, direction)
        return img, (img1, img2)
    except IOError:
        print("The received content is not a valid image.")


def get_image_file(file_path):
    img = Image.open(file_path)
    direction = Direction.HORIZONTAL if random.random() > 0.5 else Direction.VERTICAL
    img1, img2 = split_image(img, direction)
    return img, (img1, img2)


def get_image_sides(img):
    sides = {
        "north": img[0, :],
        "south": img[-1, :],
        "east": img[:, -1],
        "west": img[:, 0],
    }
    return sides


from PIL import Image


def concat_images(original_img1, original_img2):
    img1 = np.array(original_img1.convert("RGB"))
    img2 = np.array(original_img2.convert("RGB"))

    img1_sides = get_image_sides(img1)
    img2_sides = get_image_sides(img2)

    print((np.sum(img1_sides["south"] - img2_sides["north"], axis=1) ** 2).shape)
    horizontal_difference = np.sum(
        np.sqrt(np.sum((img1_sides["south"] - img2_sides["north"]) ** 2, axis=1))
    )
    vertical_difference = np.sum(
        np.sqrt(np.sum((img1_sides["east"] - img2_sides["west"]) ** 2, axis=1))
    )

    if horizontal_difference < vertical_difference:
        concat_img = np.concatenate((img1, img2), axis=0)
    else:
        concat_img = np.concatenate((img1, img2), axis=1)

    return concat_img


def main():
    img, split_imgs = get_images_url()
    split_imgs = list(split_imgs)
    # random.shuffle(split_imgs)
    concat_img = concat_images(*split_imgs)

    plt.figure(figsize=(8, 8))

    plt.subplot(3, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis(False)

    plt.subplot(3, 2, 3)
    plt.imshow(split_imgs[0], cmap="gray")
    plt.title("Split Image 1")
    plt.axis(False)

    plt.subplot(3, 2, 4)
    plt.imshow(split_imgs[1], cmap="gray")
    plt.title("Split Image 2")
    plt.axis(False)

    plt.subplot(3, 2, 5)
    plt.imshow(concat_img, cmap="gray")
    plt.title("Concatenated Image")
    plt.axis(False)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
