import json

from flask import Blueprint, request, Response

from api.contexts.bookstore.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.contexts.bookstore.authors.domain.InvalidAuthorName import InvalidAuthorName

from api.contexts.bookstore.authors.application.AuthorCreator import AuthorCreator
from api.contexts.bookstore.authors.infrastructure.AuthorContextModule import container

author_put_routes = Blueprint('author_put_routes', __name__)


@author_put_routes.route('/authors/<author_id>', methods=['PUT'])
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
