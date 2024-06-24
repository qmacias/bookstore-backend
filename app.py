from flask import Flask, request, make_response

from src.apps.bookstore.blueprints.authors_blueprint import authors_blueprint
from src.apps.bookstore.blueprints.health_check_blueprint import health_check_blueprint

app = Flask(__name__)

app.register_blueprint(authors_blueprint)
app.register_blueprint(health_check_blueprint)


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


if __name__ == '__main__':
    app.run(load_dotenv=True)
