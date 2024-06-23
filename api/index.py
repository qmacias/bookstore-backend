from flask import Flask, request, make_response, Response

from api.apps.bookstore.routes.authors.author_get_routes import author_get_routes
from api.apps.bookstore.routes.authors.author_put_routes import author_put_routes

app = Flask(__name__)

app.register_blueprint(author_get_routes)
app.register_blueprint(author_put_routes)


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


if __name__ == '__main__':
    app.run(load_dotenv=True)
