import random
import shutil
import subprocess
import sys

from faker import Faker

if sys.platform.startswith('win'):
    from utils import avatar1 as avatar
else:
    from utils import avatar2 as avatar

try:
    from generated.prisma import Prisma
except Exception as e:
    print("GOT PRISMA ERROR...")
    print(e)
    print("GENERATING PRISMA CLIENT...")
    shutil.rmtree('/generated', ignore_errors=True)
    subprocess.call(["prisma", "py", "generate"])
    subprocess.call(["prisma", "py", "fetch"])
    subprocess.call(["prisma", "db", "push"])
    print("GENERATED PRISMA CLIENT...")
    from generated.prisma import Prisma
finally:
    from generated.prisma import Base64
    from generated.prisma.models import Post


Faker.seed(random.randint(1, 1_000_000))
fake = Faker(locale="en_US")


def init_connection() -> Prisma:
    db = Prisma()
    db.connect()
    return db


def clear_table(db: Prisma) -> bool:
    db.post.delete_many()
    return True


def get_all_posts(db: Prisma):
    posts = db.post.find_many()
    return posts


def get_all_posts_sorted_desc(db: Prisma, by: str="created"):
    posts = db.post.find_many(order={by: "desc"})
    return posts


def get_all_posts_sorted_asc(db: Prisma, by: str="created"):
    posts = db.post.find_many(order={by: "asc"})
    return posts


def get_single_post(db: Prisma, id_: int):
    post = db.post.find_first(where={"id": id_})
    return post


def generate_fake_post(db: Prisma) -> bool:
    author = f"{fake.first_name()} {fake.last_name()}"
    db.post.create({
        "title": fake.sentence(nb_words=7).strip("."),
        "content": fake.paragraph(nb_sentences=30),
        "author": author,
        "avatar": Base64.encode(avatar.generate_thumbnail_bytes(string=author, size=128)),
    })
    return True


def delete_post(db: Prisma, id_: int=None) -> bool:
    success = False
    if id_:
        db.post.delete(where={"id": id_})
        success = True
    return success


def get_oldest_post(db: Prisma):
    post = db.post.find_first(order={"created": "asc"})
    return post


def get_newest_post(db: Prisma):
    post = db.post.find_first(order={"created": "desc"})
    return post


def get_random_post(db: Prisma):
    post = db.query_first(
        '''
        SELECT *
        FROM post
        ORDER BY RANDOM()
        LIMIT 1
        ''',
        model = Post
    )
    return post


def get_post_count(db: Prisma):
    count = db.post.count()
    return count


def main():
    db = init_connection()
    clear_table(db)
    for _ in range(30):
        generate_fake_post(db)
    print(get_post_count(db))


if __name__ == "__main__":
    main()
