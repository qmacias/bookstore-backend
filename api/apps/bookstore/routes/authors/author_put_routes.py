from flask import Blueprint, request, jsonify

from api.contexts.bookstore.authors.domain.id.AuthorIdNotValid import AuthorIdNotValid
from api.contexts.bookstore.authors.domain.name.AuthorNameNotValid import AuthorNameNotValid
from api.contexts.bookstore.authors.domain.AuthorAlreadyExists import AuthorAlreadyExists

from api.apps.bookstore.deps.BookstoreModule import container
from api.contexts.bookstore.authors.application.AuthorCreator import AuthorCreator

author_put_routes = Blueprint('author_put_routes', __name__)


@author_put_routes.route('/authors/<author_id>', methods=['PUT'])
def create_author(author_id):
    try:
        data = request.get_json()

        container.get(AuthorCreator).create(author_id, data.get('name'))

        return '', 201, {'Location': f'/authors/{author_id}'}
    except (AuthorAlreadyExists, AuthorIdNotValid, AuthorNameNotValid) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'/authors/{author_id}'}
