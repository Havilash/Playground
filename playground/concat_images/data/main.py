from PIL import Image


def create_test_image():
    img = Image.new("RGB", (4, 4))

    for x in range(img.width):
        for y in range(img.height):
            img.putpixel(
                (x, y),
                (
                    int(255 * x * y / img.width / img.height),
                    int(255 * x * y / img.width / img.height),
                    int(255 * x * y / img.width / img.height),
                ),
            )

    img.save("image.png")


if __name__ == "__main__":
    create_test_image()
