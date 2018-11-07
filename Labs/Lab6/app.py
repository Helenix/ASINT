from flask import Flask
from flask import render_template
from flask import request
import bookDB

app = Flask(__name__)
db = bookDB.bookDB("mylib")

@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books = count)

@app.route('/addBooksForm')
def add_book_form():
    return render_template("addBookFormTemplate.html")

@app.route('/addBook', methods=['POST', 'GET'])
def add_book():
    if request.method == "GET":
        book = request.args
    else:
        book = request.form

    db.addBook(book["Author"], book["Title"], book["Year"])

    return render_template("addBookFormTemplate.html")

@app.route('/listAllBooks')
def list_All_Books():
    books = db.listAllBooks()

    return render_template("listAllBooksTemplate.html", books = books)

@app.route('/showBookForm')
def search_book_form():
    return render_template("showBookFormTemplate.html")

@app.route('/showBook', methods = ['GET'])
def show_book():
    bid = int(request.args['id'])
    book = db.showBook(bid)

    return render_template("showBookTemplate.html", book = book)

@app.route('/listBooksAuthorForm')
def search_book_by_author_form():
    return render_template("listBooksAuthorFormTemplate.html")

@app.route('/listBooksAuthor', methods = ['GET'])
def search_book_by_author():
    author = request.args['author']
    books =  db.listBooksAuthor(author)

    return render_template("listBooksAuthorTemplate.html", author = author, books = books)

@app.route('/listBooksYearForm')
def search_book_by_year_form():
    return render_template("listBooksYearFormTemplate.html")

@app.route('/listBooksYear', methods = ['GET'])
def search_book_by_year():
    year = request.args['year']
    books =  db.listBooksYear(year)

    return render_template("listBooksYearTemplate.html", year = year, books = books)


if __name__ == '__main__':
    app.run()
