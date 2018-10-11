import pickle

class BookDB:
    def __init__(self):
        try:
            file = open("books.txt", "rb")
        except IOError:
            print("No backup file, initializing an empty database...")
            self.books = []
        else:
            print("Loading database from text file...")
            self.books = pickle.load(file)

    def insertBook(self, book):
        self.books.append(book)
        file = open("books.txt", "wb")
        pickle.dump(self.books, file)

    def showBook(self, identifier):
        for book in self.books:
            if book.identifier == identifier:
                return book
        return None

    def listAuthors(self):
        authorList = []

        for book in self.books:
            if book.author not in authorList:
                authorList.append(book.author)
        return authorList

    def listBooksPerAuthor(self, author):
        booksPerAuthorList = []
        
        for book in self.books:
            if book.author == author:
                booksPerAuthorList.append(book)
        return booksPerAuthorList

    def listBooksPerYear(self, year):
        booksPerYearList = []

        for book in self.books:
            if book.year == year:
                booksPerYearList.append(book)
        return booksPerYearList
