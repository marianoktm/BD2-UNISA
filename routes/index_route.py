from flask import Blueprint, render_template

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    # Define buttons as a list of dictionaries
    buttons_gestionelibri = [
        {"label": "Inserisci Nuovo Libro", "action": "/insert_books", "method": "get"},
        {"label": "Vai alla Lista Libri", "action": "/list", "method": "get"},
        {"label": "Libri Disponibili al Prestito", "action": "/available_books", "method": "get"},
        {"label": "Libri Presi in Prestito", "action": "/borrowed_books", "method": "get"},
        {"label": "Elimina un Libro", "action": "/delete_books", "method": "get"}
    ]

    buttons_gestioneprestiti = []

    return render_template('new/home.html', btn_libri=buttons_gestionelibri, btn_prestiti=buttons_gestioneprestiti)
