from flask import Blueprint, request

health_check_blueprint = Blueprint('health_check_blueprint', __name__)


@health_check_blueprint.route('/health_check', methods=['GET'])
def health_check():
    return '', 200, {'Location': f'{request.url_rule.rule}'}
