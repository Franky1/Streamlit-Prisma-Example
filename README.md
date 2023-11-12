<!-- markdownlint-disable MD026 -->
# Streamlit Prisma Database ORM Example Project :gem:

[![Streamlit](https://img.shields.io/badge/Go%20To-Streamlit%20Cloud-red?logo=streamlit)](https://streamlit.io/)

## :construction: :construction: :construction: *WIP - Just started - Not ready for use yet* :construction: :construction: :construction:

## Description :pencil2:

> Describe your streamlit project here.

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

---

## Status :heavy_check_mark:

:construction: :construction: :construction: *WIP - Just started - Not ready for use yet* :construction: :construction: :construction:

> Last changed: 2023-11-12

## Issues :bug:

- Caching does not work for the posts list

## ToDo :ballot_box_with_check:

- [ ] Add documentation
- [ ] Finish example project
- [ ] Add some CSS styling
- [ ] Deploy to streamlit cloud
- [ ] Clean up repository

## Ideas :bulb:

- Make a full example with an external database

## Resources :books:

- Prisma :heart:
  - <https://www.prisma.io/>
  - <https://www.prisma.io/ecosystem>
  - <https://github.com/prisma/prisma>
- Prisma Client Python :heart:
  - <https://prisma-client-py.readthedocs.io/en/stable/>
  - <https://github.com/RobertCraigie/prisma-client-py>
