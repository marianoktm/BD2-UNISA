from flask import Flask, render_template, request
from pymongo import MongoClient
import mongodb_config
from routes import index_route, form_route


def init_flask_app():
    mongoClient = MongoClient(mongodb_config.connection_string)

    mongoDatabase = mongoClient['project']
    studentsCollection = mongoDatabase['students']
    booksCollection = mongoDatabase['books']

    flaskApp = Flask(__name__)

    flaskApp.register_blueprint(index_route.indexBlueprint)
    flaskApp.register_blueprint(form_route.formBlueprint)

    return flaskApp


if __name__ == '__main__':
    app = init_flask_app()
    app.run(debug=True)
