from flask import Flask
from routes import available_books_route, borrowed_books_route, borrow_books_route, index_route, list_books_route, \
    insert_students_route, insert_books_route, delete_books_route, error_handler, return_books

import db.mongodb_config

def init_flask_app():
    flaskApp = Flask(__name__)

    # index
    flaskApp.register_blueprint(index_route.indexBlueprint)

    # insert_students
    flaskApp.register_blueprint(insert_students_route.studentsBlueprint)

    # insert_books
    flaskApp.register_blueprint(insert_books_route.booksBlueprint)

    # delete_books
    flaskApp.register_blueprint(delete_books_route.delete_booksBlueprint)

    # view list
    flaskApp.register_blueprint(list_books_route.listBlueprint)

    # borrow books
    flaskApp.register_blueprint(borrow_books_route.borrowBlueprint)

    # borrowed books
    flaskApp.register_blueprint(borrowed_books_route.borrowedBlueprint)

    # available books
    flaskApp.register_blueprint(available_books_route.availableBlueprint)

    # error handler
    flaskApp.register_blueprint(error_handler.error_blueprint)

    #return books
    flaskApp.register_blueprint(return_books.returnBlueprint)

    return flaskApp


if __name__ == '__main__':
    app = init_flask_app()
    app.run(debug=True)
