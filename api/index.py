import json

from flask import Flask, request, make_response, Response

from api.authors.application.AuthorCreator import AuthorCreator
from api.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.authors.domain.InvalidAuthorName import InvalidAuthorName
from api.authors.infrastructure.AuthorWiringModule import container

app = Flask(__name__)


@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response


@app.route('/health_check', methods=['GET'])
def health_check():
    return Response(
        '', 200, {
            'Content-Type': 'application/json', 'Location': f'{request.url_rule.rule}'
        }
    )


@app.route('/authors/<author_id>', methods=['PUT'])
def create_author(author_id):
    try:
        data = request.get_json()

        container.get(AuthorCreator).create(author_id, data.get('name'))

        return Response(
            '', 201, {
                'Content-Type': 'application/json', 'Location': f'/authors/{author_id}'
            }
        )
    except (InvalidAuthorId, InvalidAuthorName) as e:
        return Response(
            json.dumps({'error': str(e)}), 400, {
                'Content-Type': 'application/json', 'Location': f'/authors/{author_id}'
            }
        )


if __name__ == '__main__':
    app.run(load_dotenv=True)
