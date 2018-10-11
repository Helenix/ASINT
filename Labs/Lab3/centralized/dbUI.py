from book import Book

class dbUI:
    def __init__(self, db):
        self.db = db

        while True:
            print("\033[92m" + "Valid commands:" + "\033[0m")
            print("\033[92m" + "NEW (or 1)" + "\033[0m")
            print("\033[92m" + "SHOW (or 2)" + "\033[0m")
            print("\033[92m" + "AUTHORS (or 3)" + "\033[0m")
            print("\033[92m" + "SEARCH_AUTHOR (or 4)" + "\033[0m")
            print("\033[92m" + "SEARCH_YEAR (or 5)" + "\033[0m")
            print("\033[92m" + "'q' for quit..."  + "\033[0m")
            cmd = input("Insert command: ")

            if cmd == "NEW" or cmd == '1' :   
                author = input("Author: ")
                title = input("Title: ") 
                year = int(input("Year: "))  
                identifier = int(input("ID: "))     
                self.db.insertBook(Book(author, title, year, identifier))
            
            elif cmd == "SHOW" or cmd == '2':
                identifier = int(input("ID: ")) 
                book = self.db.showBook(identifier)
                if book != None:
                    print("-> Book author: %s" %(book.author))
                    print("-> Book title: %s" %(book.title))
                    print("-> Book year: %d" %(book.year))
                else:
                    print("-> No match found for that book ID!")
                
            elif cmd == "AUTHORS" or cmd == '3': 
                authorList = self.db.listAuthors()
                if authorList:
                    print("Authors found:")
                    for author in authorList:
                        print("-> %s" %(author))
                else:
                    print("No authors found!")

            elif cmd == "SEARCH_AUTHOR" or cmd == '4':    
                author = input("Author: ")
                booksPerAuthorList = self.db.listBooksPerAuthor(author)

                if booksPerAuthorList:
                    print("Books from author %s:" %(author))  
                    for book in booksPerAuthorList:
                        print("-> Title: %s Year: %d" %(book.title, book.year))
                else:
                    print("No books found from author %s!" %(author))  


            elif cmd == "SEARCH_YEAR" or cmd == '5':
                year = int(input("Year: "))
                booksPerYearList = self.db.listBooksPerYear(year)

                if booksPerYearList:
                    print("Books from year %d:" %(year))  
                    for book in booksPerYearList:
                        print("-> Author: %s Title: %s" %(book.author, book.title))
                else:
                    print("No books found from year %d!" %(year))

            elif cmd == 'q':    
                break

    