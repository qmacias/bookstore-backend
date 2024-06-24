from types import MappingProxyType
from flask import Blueprint, jsonify, request

from api.apps.bookstore.BookstoreModule import container

from api.contexts.bookstore.authors.application.AuthorCreator import AuthorCreator
from api.contexts.bookstore.authors.application.AuthorRemover import AuthorRemover
from api.contexts.bookstore.authors.application.AuthorSearcher import AuthorSearcher
from api.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from api.contexts.bookstore.authors.domain.AuthorNameNotValid import AuthorNameNotValid
from api.contexts.bookstore.authors.domain.AuthorAlreadyExists import AuthorAlreadyExists
from api.contexts.bookstore.authors.domain.AuthorDoesNotExists import AuthorDoesNotExists

authors_blueprint = Blueprint('authors_blueprint', __name__)


@authors_blueprint.route('/authors/<author_id>', methods=['PUT'])
def create_author(author_id):
    try:
        data = request.get_json()

        container.get(AuthorCreator).create(author_id, data.get('name'))

        return '', 201, {'Location': f'/authors/{author_id}'}
    except (AuthorIdNotValid, AuthorNameNotValid, AuthorAlreadyExists) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'/authors/{author_id}'}


@authors_blueprint.route('/authors/<author_id>', methods=['GET'])
def search_author(author_id):
    try:
        author: MappingProxyType = (
            container.get(AuthorSearcher).search(author_id)
        )

        return jsonify(dict(author)), 200, {'Location': f'/authors/{author_id}'}
    except (AuthorIdNotValid, AuthorDoesNotExists) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'/authors/{author_id}'}


@authors_blueprint.route('/authors/<author_id>', methods=['DELETE'])
def remove_author(author_id):
    try:
        container.get(AuthorRemover).remove(author_id)

        return '', 200, {'Location': f'/authors/{author_id}'}
    except (AuthorIdNotValid, AuthorDoesNotExists) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'/authors/{author_id}'}
