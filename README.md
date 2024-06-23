# Getting Started

We're using Python v3.10.0 and Flask v3.0.3

## Bookstore routes

Here the client interacts with the provided Flask API endpoints.

| Method | Url                                       | Description      |
|--------|-------------------------------------------|------------------|
| GET    | http://127.0.0.1:5000/health_check        | Health check     |
| PUT    | http://127.0.0.1:5000/authors/{author_id} | Create an author |

---

Health check
```bash
http http://127.0.0.1:5000/health_check
```

Create an author
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```

(*) Create an (invalid) author

{ "error": "Invalid author id 'cea03186-4606-432c-8d16-ed47276cae5.'" }

ERROR:AuthorIdFormatException: invalid literal for int() with base 16: 'cea031864606432c8d16ed47276cae5.'
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5.
```
{ "error": "Invalid author id 'cea03186-4606-432c-8d16-ed47276cae5d.'" }

ERROR:AuthorIdFormatException: badly formed hexadecimal UUID string
```bash
echo '{"name": "John Doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d.
```
{ "error": "Invalid author name 'john_doe'" }

ERROR:AuthorNameMatchException: no matches for 'john_doe'
```bash
echo '{"name": "john_doe"}' | http PUT http://127.0.0.1:5000/authors/cea03186-4606-432c-8d16-ed47276cae5d
```
