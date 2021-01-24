import datetime
class Library:
    def __init__(self,listofbooks,library_name):
        date_time = datetime.datetime.today()
        self.lendedbooklist = {}
        self.listofbooks = listofbooks
        self.library_name= library_name

    def displaybooks(self):
        print(f"\n We have following books in our: {self.library_name}\n")
        for books in listofbooks:
            print(books)

    def lendbooks(self,name,book_name):
            if book_name in self.listofbooks:
                self.lendedbooklist[book_name] = [name,datetime.datetime.today().strftime("%H:%M:%S %h,%d,%Y")]
                self.listofbooks.remove(book_name)
                print("Lended")
            else:
                try:
                    print(f"Sorry the book is borrowed by {self.lendedbooklist[book_name][0]}")
                except KeyError:
                    print("Sorry The book is not available in the library stock: ")
                except Exception as e:
                    print(e)

    def donate(self,bookdonatename):
        self.listofbooks.append(bookdonatename)

    def returnbook(self,clnt_name,book):
            if book not in self.listofbooks:
                try:
                    if clnt_name == self.lendedbooklist[book][0]:
                        self.lendedbooklist.pop(book)
                        self.listofbooks.append(book)
                        print("Returned")
                    else:
                        print("Your Name doesn't Matches in our Records, Please enter your name Correctly:")
                except KeyError:
                    print("You cannot return the book because the book is either not in our Library or it is not lended by you:")

            else:
                try:
                    if book in self.listofbooks:
                        print("You cannot return the book because the book is not lended by you")
                except Exception as e:
                    print(e)

    def deletebook(self,bookname):
        try:
            self.listofbooks.remove(bookname)
            print("Deleted")
        except ValueError:
            print("Book is not in Library")

    def lendedbooklist1(self):
        if not self.lendedbooklist:
            print("No book lended!!!")
        else:         
            for key,values in self.lendedbooklist.items():
                print(f"{values[0]} has taken {key} on {values[1]}") 