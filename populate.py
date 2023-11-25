from utils import database


def main():
    db = database.init_connection()
    database.clear_table(db=db)
    for _ in range(30):
        database.generate_fake_post(db=db)
    print(database.get_post_count(db=db))


if __name__ == "__main__":
    main()
