import io

from PIL import Image

from utils import database


def show_image(image_byte):
    """show image with pillow"""
    image = Image.open(io.BytesIO(image_byte), formats=['PNG'])
    image.show()


def main():
    db = database.init_connection()
    post = database.get_random_post(db=db)
    print(post.created, post.author, type(post.avatar))
    show_image(image_byte=post.avatar.decode())


if __name__ == "__main__":
    main()
