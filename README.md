# Getting Started

We're using Python v3.10.0 and Flask v3.0.3

## Bookstore routes

Here the client interacts with the provided Flask API endpoints.

| Method | Url                                                   | Description      |
|--------|-------------------------------------------------------|------------------|
| GET    | http://qmacias.pythonanywhere.com/health_check        | Health check     |
| GET    | http://qmacias.pythonanywhere.com/authors             | Search authors   |
| POST   | http://qmacias.pythonanywhere.com/authors             | Create an author |
| PUT    | http://qmacias.pythonanywhere.com/authors/{author_id} | Modify an author |
| GET    | http://qmacias.pythonanywhere.com/authors/{author_id} | Search an author |
| DELETE | http://qmacias.pythonanywhere.com/authors/{author_id} | Remove an author |

---

Health check
```bash
http GET http://qmacias.pythonanywhere.com/health_check
```

Search authors:
```bash
http GET http://qmacias.pythonanywhere.com/authors
```

Create an author
```bash
echo '{"name": "John Doe"}' | http POST http://qmacias.pythonanywhere.com/authors
```

(*) Create an author

{"error": "Author name 'None' not valid."}

ERROR:AuthorNameNotValidType: 'NoneType' object has no attribute 'strip'
```bash
echo '{}' | http POST http://qmacias.pythonanywhere.com/authors
```
{"error": "Author name '' not valid."}

ERROR:AuthorNameNotValidPattern: no pattern for ''
```bash
echo '{"name": ""}' | http POST http://qmacias.pythonanywhere.com/authors
```
{"error": "Author name 'john_doe' not valid."}

ERROR:AuthorNameNotValidPattern: no pattern for 'john_doe'
```bash
echo '{"name": "john_doe"}' | http POST http://qmacias.pythonanywhere.com/authors
```
{"error": "Author name 'John Doe' already exists."}

ERROR:AuthorNameAlreadyExistsIntegrity: 1062 (23000): Duplicate entry 'John Doe' for key 'authors.name'
```bash
echo '{"name": "John Doe"}' | http POST http://qmacias.pythonanywhere.com/authors
```

Modify an author
```bash
echo '{"name": "Margaret Jones"}' | http PUT http://qmacias.pythonanywhere.com/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

(*) Modify an author

{"error": "Author id 'cea03186-4606-432c-8d16-ed47276cae5.' not valid."}

ERROR:AuthorIdNotValidFormat: invalid literal for int() with base 16: 'cea031864606432c8d16ed47276cae5.'
```bash
echo '{"name": "Margaret Jones"}' | http PUT http://qmacias.pythonanywhere.com/authors/cea03186-4606-432c-8d16-ed47276cae5.
```
{"error": "Author id 'cea03186-4606-432c-8d16-ed47276cae5d.' not valid."}

ERROR:AuthorIdNotValidFormat: badly formed hexadecimal UUID string
```bash
echo '{"name": "Margaret Jones"}' | http PUT http://qmacias.pythonanywhere.com/authors/cea03186-4606-432c-8d16-ed47276cae5d.
```

Search an author
```bash
http GET http://qmacias.pythonanywhere.com/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

(*) Search an author

{"error": "Author 'd77fafb5-701e-40b7-b73d-9832a24ed968' does not exist."}

ERROR:AuthorDoesNotExistsUnknown: unknown registry: 'd77fafb5-701e-40b7-b73d-9832a24ed968'
```bash
http GET http://qmacias.pythonanywhere.com/authors/d77fafb5-701e-40b7-b73d-9832a24ed968
```

Remove an author
```bash
http DELETE http://qmacias.pythonanywhere.com/authors/cea03186-4606-432c-8d16-ed47276cae5d
```
