from types import MappingProxyType
from flask import Blueprint, jsonify

from api.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from api.contexts.bookstore.authors.domain.AuthorDoesNotExists import AuthorDoesNotExists

from api.apps.bookstore.deps.BookstoreModule import container
from api.contexts.bookstore.authors.application.AuthorSearcher import AuthorSearcher

author_get_routes = Blueprint('author_get_routes', __name__)


@author_get_routes.route('/authors/<author_id>', methods=['GET'])
def search_author(author_id):
    try:
        author: MappingProxyType = (
            container.get(AuthorSearcher).search(author_id)
        )

        return jsonify(dict(author)), 200, {'Location': f'/authors/{author_id}'}
    except (AuthorIdNotValid, AuthorDoesNotExists) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'/authors/{author_id}'}
