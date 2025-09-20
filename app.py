from flask import Flask
from routes import index_route, list_books_route, insert_students_route, insert_books_route, delete_books_route


def init_flask_app():


    flaskApp = Flask(__name__)

    #index
    flaskApp.register_blueprint(index_route.indexBlueprint)

    #insert_students
    flaskApp.register_blueprint(insert_students_route.studentsBlueprint)

    #insert_books
    flaskApp.register_blueprint(insert_books_route.booksBlueprint)

    #delete_books
    flaskApp.register_blueprint(delete_books_route.delete_booksBlueprint)

    #view list
    flaskApp.register_blueprint(list_books_route.listBlueprint)

    return flaskApp


if __name__ == '__main__':
    app = init_flask_app()
    app.run(debug=True)
