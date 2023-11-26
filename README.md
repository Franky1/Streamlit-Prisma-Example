<!-- markdownlint-disable MD026 -->
# Streamlit Prisma Database ORM Example Project :gem:

[![Streamlit](https://img.shields.io/badge/Go%20To-Streamlit%20Cloud-red?logo=streamlit)](https://app-prisma-example-fogbht3q5abmltqhnw2cbh.streamlit.app/)

## :construction: *WIP* :construction:

Streamlit example app with Prisma Database ORM.

## Description :pencil2:

This Streamlit app is only a simple example of how to use Prisma Database ORM with Streamlit.
It uses a local SQLite database to store the data.
This app is a simple post generator with fake data.
Random posts are generated with the `Faker` library and the `py-avataaars` library is used to generate avatars.
You can add random posts, delete posts and delete all posts.

## ToDo :ballot_box_with_check:

- [ ] Add more CSS styling for the Streamlit app
- [ ] Test Streamlit app on Streamlit Cloud from different clients

## Ideas :bulb:

- Make example with an external database instead of local SQLite

## Issues :bug:

- Prisma Setup/Init on Streamlit Cloud is a bit tricky
- This app only uses a local SQLite database, there is no external database connection, therefore data is not persistent.

## Status

:construction: *WIP* :construction:

> Last changed: 2023-11-26

## Prisma Setup :gem:

### Prisma Schema

```prisma
datasource db {
  provider = "sqlite"
  url      = "file:posts.sqlite"
}

generator client {
  provider             = "prisma-client-py"
  interface            = "sync"
  recursive_type_depth = 5
  output               = "./generated/prisma"
  binaryTargets        = ["native", "debian-openssl-1.1.x", "debian-openssl-3.0.x"]
}

model Post {
  id      Int      @id @default(autoincrement())
  uuid    String   @unique @default(uuid())
  created DateTime @default(now())
  author  String
  title   String
  content String?
  avatar  Bytes?
}
```

## Resources :books:

- Prisma
  - <https://www.prisma.io/>
  - <https://www.prisma.io/ecosystem>
  - <https://github.com/prisma/prisma>
- Prisma Client Python
  - <https://prisma-client-py.readthedocs.io/en/stable/>
  - <https://github.com/RobertCraigie/prisma-client-py>

## Links :link:

- <https://pub.towardsai.net/build-real-time-data-applications-quickly-using-streamlit-and-prisma-ef6e6af81e30>
- <https://github.com/vatsalsaglani/Streamlit-Prisma>
- <https://discuss.streamlit.io/t/app-with-prisma-doesnt-work-anymore/49736>
- <https://github.com/Wazarr94/prisma-streamlit-example>
- <https://discuss.streamlit.io/t/running-a-command-before-deploying/31661>
- <https://discuss.streamlit.io/t/from-prisma-import-prismafile-raise-runtimeerrorr/55124>
