<!-- markdownlint-disable MD026 -->
# Streamlit Prisma Database ORM Example Project :gem:

## :construction: :construction: :construction: *Project halted* :construction: :construction: :construction:

Due to numerous problems with the Prisma Python client, the project was put on hold for the time being. The Python client was not stable and does not yet appear to be fully developed. In particular, the setup of the Prisma Python client in an environment such as Streamlit Cloud did not work. The binaries cannot be installed via apt. There are too many things running in the background that you can't control. There are dependencies on Node and Rust.

## Issues :bug:

- Prisma Client Python did not work stable
- Prisma Setup/Init on Streamlit Cloud did not work
- Dependencies on Node and Rust
- Caching does not work for the posts list

## Status

:construction: :construction: :construction: *Project halted* :construction: :construction: :construction:

> Last changed: 2023-11-25

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
  output               = "./prisma_client"
}

model Post {
  id      BigInt      @id @default(autoincrement())
  uuid    String      @unique @default(uuid())
  created DateTime    @default(now())
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
