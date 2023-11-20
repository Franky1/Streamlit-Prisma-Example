<!-- markdownlint-disable MD026 -->
# Streamlit Prisma Database ORM Example Project :gem:

## :construction: :construction: :construction: *Project abandoned* :construction: :construction: :construction:

Due to numerous problems with the Prisma Python client, the project was put on hold for the time being. The Python client was not stable and does not yet appear to be fully developed. In particular, the setup of the Prisma Python client in an environment such as Streamlit Cloud did not work. The binaries cannot be installed via apt. There are too many things running in the background that you can't control. There are dependencies on Node and Rust.

## Issues :bug:

- Prisma Client Python did not work stable
- Prisma Setup/Init on Streamlit Cloud did not work
- Dependencies on Node and Rust
- Caching does not work for the posts list

## Status

:construction: :construction: :construction: *Project abandoned* :construction: :construction: :construction:

> Last changed: 2023-11-20

---

## Prisma Setup :gem:

### Prisma Schema

```prsima
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
  id         String   @id @default(cuid())
  created_at DateTime @default(now())
  author     String
  avatar     String?
  title      String
  content    String?
}
```

### Prisma Client Generator

```bash
prisma generate
```

### Prisma Database Migration

```bash
prisma db push --skip-generate
```

## Resources :books:

- Prisma :heart:
  - <https://www.prisma.io/>
  - <https://www.prisma.io/ecosystem>
  - <https://github.com/prisma/prisma>
- Prisma Client Python :heart:
  - <https://prisma-client-py.readthedocs.io/en/stable/>
  - <https://github.com/RobertCraigie/prisma-client-py>
