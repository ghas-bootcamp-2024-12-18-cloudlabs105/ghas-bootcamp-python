
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE '%" + name + "%'"
        )
        books = [Book(*row) for row in cursor]
        if len(books) == 0:
            return make_response(f"Search Result not found: {name}", 404)

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + author + "%'"
        )
        books = [Book(*row) for row in cursor]
        if len(books) == 0:
            return make_response(f"Search Result not found: {author}", 404)

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)