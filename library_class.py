import datetime

class Library:
    def __init__(self,listofbooks,library_name):
        date_time = datetime.datetime.today()
        self.borrowedbooklist = {}
        self.listofbooks = listofbooks
        self.library_name = library_name

    def displaybooks(self):
        print(f"\n We have following books in our: {self.library_name}\n")
        for books in self.listofbooks:
            print(books)

    def searchbookbytitle(self,book_name):
        if book_name in self.listofbooks:
            print("Here is your search result:-\n")
            print(book_name)
        else:
            print("No results found")

    def borrowbooks(self,name,book_name):
            if book_name in self.listofbooks:
                self.borrowedbooklist[book_name] = [name,datetime.datetime.today().strftime("%H:%M:%S %h,%d,%Y")]
                self.listofbooks.remove(book_name)
                print("Borrowed")
            else:
                try:
                    print(f"Sorry the book is borrowed by {self.borrowedbooklist[book_name][0]}")
                except KeyError:
                    print("Sorry The book is not available in the library stock: ")
                except Exception as e:
                    print(e)

    def donate(self,bookdonatename):
        self.listofbooks.append(bookdonatename)

    def returnbook(self,clnt_name,book):
            if book not in self.listofbooks:
                try:
                    if clnt_name == self.borrowedbooklist[book][0]:
                        self.borrowedbooklist.pop(book)
                        self.listofbooks.append(book)
                        print("Returned")
                    else:
                        print("Your Name doesn't Matches in our Records, Please enter your name Correctly:")
                except KeyError:
                    print("You cannot return the book because the book is either not in our Library or it is not lended by you:")

            else:
                try:
                    if book in self.listofbooks:
                        print("You cannot return the book because the book is not borrowed by you")
                except Exception as e:
                    print(e)

    def deletebook(self,bookname):
        try:
            self.listofbooks.remove(bookname)
            print("Deleted")
        except ValueError:
            print("Book is not in Library")

    def borrowedbooklist1(self):
        if not self.borrowedbooklist:
            print("No book borrowed!!!")
        else:         
            for key,values in self.borrowedbooklist.items():
                print(f"{values[0]} has taken {key} on {values[1]}") 