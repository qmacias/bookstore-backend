# Getting Started

We're using Python v3.10.0 and Flask v3.0.3

## Bookstore routes

Here the client interacts with the provided Flask API endpoints.

| Method | Url                                       | Description      |
|--------|-------------------------------------------|------------------|
| GET    | http://127.0.0.1:5000/health_check        | Health check     |
| PUT    | http://127.0.0.1:5000/authors/{author_id} | Create an author |
| GET    | http://127.0.0.1:5000/authors/{author_id} | Search an author |
| DELETE | http://127.0.0.1:5000/authors/{author_id} | Remove an author |

---

Health check
```bash
http GET http://127.0.0.1:5000/health_check
```

Create an author
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

(*) Create an (invalid) author

{"error": "Author 'cea03186-4606-432c-8d16-ed47276cae5d' already exists."}

ERROR:AuthorLookUpConflict: author lookup conflict: cea03186-4606-432c-8d16-ed47276cae5d
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```
{"error": "Author id 'cea03186-4606-432c-8d16-ed47276cae5.' not valid."}

ERROR:AuthorIdNotValidFormat: invalid literal for int() with base 16: 'cea031864606432c8d16ed47276cae5.'
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5.
```
{"error": "Author id 'cea03186-4606-432c-8d16-ed47276cae5d.' not valid."}

ERROR:AuthorIdNotValidFormat: badly formed hexadecimal UUID string
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d.
```
{"error": "Author name 'john_doe' is not valid."}

ERROR:AuthorNameNotValidPattern: no pattern for 'john_doe'
```bash
echo '{"name": "john_doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

Search an author
```bash
http GET http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

(*) Search an (unknown) author

{"error": "Author 'd77fafb5-701e-40b7-b73d-9832a24ed968' does not exist."}

ERROR:AuthorLookUpFailed: author lookup failed: 'd77fafb5-701e-40b7-b73d-9832a24ed968'
```bash
http GET http://127.0.0.1:5000/authors/d77fafb5-701e-40b7-b73d-9832a24ed968
```

Remove an author
```bash
http DELETE http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

(*) Remove an (unknown) author

{"error": "Author 'd77fafb5-701e-40b7-b73d-9832a24ed968' does not exist."}

ERROR:AuthorLookUpFailed: author lookup failed: 'd77fafb5-701e-40b7-b73d-9832a24ed968'
```bash
http DELETE http://127.0.0.1:5000/authors/d77fafb5-701e-40b7-b73d-9832a24ed968
```
