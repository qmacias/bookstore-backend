from flask import Blueprint, jsonify

from api.contexts.bookstore.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.contexts.bookstore.authors.domain.AuthorDoesNotExist import AuthorDoesNotExist

from api.apps.bookstore.deps.BookstoreModule import container
from api.contexts.bookstore.authors.application.AuthorRemover import AuthorRemover

author_del_routes = Blueprint('author_del_routes', __name__)


@author_del_routes.route('/authors/<author_id>', methods=['DELETE'])
def remove_author(author_id):
    try:
        container.get(AuthorRemover).remove(author_id)

        return '', 200, {'Location': f'/authors/{author_id}'}
    except (AuthorDoesNotExist, InvalidAuthorId) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'/authors/{author_id}'}
