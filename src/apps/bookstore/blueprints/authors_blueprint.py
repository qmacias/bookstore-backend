from typing import Sequence
from types import MappingProxyType

from flask import Blueprint, jsonify, request

from src.apps.bookstore.BookstoreModule import container
from src.contexts.bookstore.authors.application.AuthorCreator import AuthorCreator
from src.contexts.bookstore.authors.application.AuthorModifier import AuthorModifier
from src.contexts.bookstore.authors.application.AuthorRemover import AuthorRemover
from src.contexts.bookstore.authors.application.AuthorSearcher import AuthorSearcher
from src.contexts.bookstore.authors.application.AuthorsSearcher import AuthorsSearcher
from src.contexts.bookstore.authors.domain.AuthorDoesNotExists import AuthorDoesNotExists
from src.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from src.contexts.bookstore.authors.domain.AuthorNameAlreadyExists import AuthorNameAlreadyExists
from src.contexts.bookstore.authors.domain.AuthorNameNotValid import AuthorNameNotValid

authors_blueprint = Blueprint('authors_blueprint', __name__)


@authors_blueprint.route('/authors', methods=['GET'])
def search_all_authors():
    authors: Sequence[MappingProxyType] = (
        container.get(AuthorsSearcher).search_all()
    )

    items = [dict(author) for author in authors]

    return jsonify(items), 200, {'Location': f'{request.url_rule.rule}'}


@authors_blueprint.route('/authors', methods=['POST'])
def create_author():
    try:
        data = request.get_json()

        container.get(AuthorCreator).create(data.get('name'))

        return '', 201, {'Location': f'{request.url_rule.rule}'}
    except (AuthorIdNotValid, AuthorNameNotValid, AuthorNameAlreadyExists) as e:
        return jsonify({'error': str(e)}), 400, {'Location': f'{request.url_rule.rule}'}


@authors_blueprint.route('/authors/<author_id>', methods=['PUT'])
def modify_author(author_id):
    try:
        data = request.get_json()

        container.get(AuthorModifier).modify(author_id, data.get('name'))

        return '', 200, {'Location': f'/authors/{author_id}'}
    except (AuthorIdNotValid, AuthorNameNotValid, AuthorDoesNotExists) as e:
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
