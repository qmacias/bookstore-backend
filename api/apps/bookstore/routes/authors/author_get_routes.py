import json

from types import MappingProxyType
from flask import Blueprint, Response

from api.contexts.bookstore.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.contexts.bookstore.authors.domain.AuthorDoesNotExist import AuthorDoesNotExist

from api.apps.bookstore.deps.BookstoreModule import container
from api.contexts.bookstore.authors.application.AuthorSearcher import AuthorSearcher

author_get_routes = Blueprint('author_get_routes', __name__)


@author_get_routes.route('/authors/<author_id>', methods=['GET'])
def search_author(author_id):
    try:
        author: MappingProxyType = container.get(AuthorSearcher).search(author_id)

        return Response(
            json.dumps(dict(author)), 200, {
                'Content-Type': 'application/json', 'Location': f'/authors/{author_id}'
            }
        )
    except (AuthorDoesNotExist, InvalidAuthorId) as e:
        return Response(
            json.dumps({'error': str(e)}), 400, {
                'Content-Type': 'application/json', 'Location': f'/authors/{author_id}'
            }
        )
