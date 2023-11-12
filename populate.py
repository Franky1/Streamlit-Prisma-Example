import random
import time

from faker import Faker

from prisma_client import Prisma

Faker.seed(random.randint(1, 1_000_000))
fake = Faker(locale="de_DE")


def get_database():
    db = Prisma()
    return db


def generate_fake_post(db):
    db.post.create({
        "title": fake.sentence(nb_words=4).strip("."),
        "content": fake.paragraph(nb_sentences=5),
        "author": fake.name()
    })


def get_all_posts(db):
    posts = db.post.find_many()
    return posts


def clear_table(db):
    db.post.delete_many()


if __name__ == "__main__":
    db = get_database()
    db.connect()
    clear_table(db)
    for _ in range(10):
        generate_fake_post(db)
        time.sleep(0.1)
    print(get_all_posts(db))
    db.disconnect()
