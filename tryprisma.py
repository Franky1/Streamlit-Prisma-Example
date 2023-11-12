from prisma_client import Prisma


def main() -> None:
    db = Prisma()
    db.connect()
    # print(db.get_metrics())
    print(db.is_connected())
    db.disconnect()


if __name__ == '__main__':
    main()
