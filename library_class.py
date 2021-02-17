import datetime
import requests

class Library:
    def __init__(self,library_name):
        date_time = datetime.datetime.today()
        self.borrowedbooklist = {}
        self.library_name = library_name


    def searchbookbytitle(self,book_title):
        r = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_title}&printType=books&key=AIzaSyD7Ja_vRi7qH1_F2iLn-GZv3nc_f0O2vdc')
        r_json = r.json()
        for i in range(len(r_json['items'])):
            print(r_json['items'][i]['volumeInfo']['title'])


    def searchbookbyisbn(self,isbn_number):
        r = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=""+isbn:{isbn_number}&key=AIzaSyD7Ja_vRi7qH1_F2iLn-GZv3nc_f0O2vdc')
        r_json = r.json()
        print(f"Book Name: {r_json['items'][0]['volumeInfo']['title']}")
        print(f"ISBN: {isbn_number}")
        for i in range(len(r_json['items'][0]['volumeInfo']['authors'])):
            print(f"Authors Name: {r_json['items'][0]['volumeInfo']['authors'][i]}")


    def searchbookbyauthor(self,author_name):
        split_author = author_name.split(" ")
        concat_author_name = '+'.join(split_author).capitalize()
        r1 = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=""+inauthor:"{concat_author_name}"&key=AIzaSyD7Ja_vRi7qH1_F2iLn-GZv3nc_f0O2vdc')
        r1_json = r1.json()
        print(f"All books that are written by {author_name}:-\n")
        for i in range(len(r1_json['items'])):
            print(r1_json['items'][i]['volumeInfo']['title'])


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
            

    def borrowedbooklist1(self):
        if not self.borrowedbooklist:
            print("No book borrowed!!!")
        else:         
            for key,values in self.borrowedbooklist.items():
                print(f"{values[0]} has taken {key} on {values[1]}") 