from library_class import Library
from Credentials import credential
username, password = credential()
          



if __name__ == '__main__':

    listofbooks = ["Python","C++","Java","Javascript","Django","Flask","Flutter","Kotlin","React","Angular","Node.js","Mongodb"]

    l1 = Library(listofbooks,"Shubham's library")

    while True:
        print(f"\n Welcome to the {l1.library_name}.\n")
        print("Press :-")
        option = int(input("1. To see the list of available books in Library\n"
                        "2. Search a book in the library\n"
                       "3. Borrow a book from Library\n"
                       "4. Return a borrowed book\n"
                       "5. Donate a book to Library\n"
                       "6. Quit\n"
                       "7. Delete a book from Library(Only for Admin)\n"
                       "8. See the list of books borrowed and by whom(Only for Admin)\n"
                       ">>> ").rstrip())

        if option == 1 :
            l1.displaybooks()

        elif option == 2:
            book_name = input("Enter the book name to Search: ").capitalize().rstrip()
            l1.searchbookbyname(book_name)

        elif option == 3:
            client_name = input("Please Provide your Full name: ").capitalize()
            book_name = input("Which book you want to Lend: ").capitalize().rstrip()
            l1.borrowbooks(client_name.lower(),book_name)

        elif option == 4:
            client_name = input("Please Provide your Full name: ")
            book_name = input("Which book you want to Return: ").capitalize().rstrip()
            l1.returnbook(client_name.lower(),book_name)

        elif option == 5:
            bookdname = input("Which book you want to Donate: ").capitalize().rstrip()
            l1.donate(bookdname)
            while True:
                op = input("Want to Donate more books enter 'y' if yes or 'n' to exit: ").rstrip()
                if op.lower() == 'n':
                    break
                elif op.lower() == 'y':
                    bookdname = input("Which book you want to Donate: ").capitalize().rstrip()
                    l1.donate(bookdname)
                else:
                    print("Wrong Input!!! Enter a valid input.")

        elif option == 6:
            exit()

        elif option == 7:
            while True:
                username_by_user = input("Enter Your User Name: ")
                password_by_user = input("Enter Your Paasword: ")
                if username_by_user == username and password_by_user == password:
                    db = input("Enter bookname which you want to delete: ").capitalize().rstrip()
                    l1.deletebook(db)
                    break
                else:
                    print("Wrong Credentials!!!")
                    option = int(input("Want to try more Press 1 otherwise Press any key to exit: "))
                    if option == 1:
                        continue
                    else:
                        break

        elif option == 8:            
             while True:
                username_by_user = input("Enter Your User Name: ")
                password_by_user = input("Enter Your Paasword: ")
                if username_by_user == username and password_by_user == password:
                    l1.borrowedbooklist1()
                    break
                else:
                    print("Wrong Credentials!!!")
                    option = int(input("Want to try more Press 1 otherwise Press any key to exit: "))
                    if option == 1:
                        continue
                    else:
                        break


        else:
            print("Wrong input, Please Enter a valid Input:").rstrip()

        user_op = ""
        while (user_op.lower() != 'q' and user_op.lower() != 'c'):
            user_op = input("\nEnter 'q' to Quit and 'c' to Continue: ").rstrip()
            if user_op.lower() == 'q':
                exit()
            elif user_op.lower() == 'c':
                continue
            else:
                print("Enter a valid input please:")












# listofbooks = {'python':
#     {
#         'isbn':'1-7632-834',
#         'author':'a'
#     },
#     'c++':
#     {
#         'isbn':'1-49857-2543',
#         'author':'b'
#     },
#     'java':
#     {
#         'isbn':'2-48573-345790',
#         'author':'c'
#     },
#     'javascript':
#     {
#         'isbn':'2-55353095-305',
#         'author':'d'
#     },
#     'django':
#     {
#         'isbn':'2-35457-25895',
#         'author':'e'
#     },
#     'flask':
#     {
#         'isbn':'2-386734-2353453',
#         'author':'f'
#     },
#     'flutter':
#     {
#         'isbn':'2-4398734-58498734',
#         'author':'g'
#     },
#     'kotlin':
#     {
#         'isbn':'2-59873653-983534',
#         'author':'h'
#     },
#     'react':
#     {
#         'isbn':'9-4587634-34975634',
#         'author':'i'
#     },
#     'angular':
#     {
#         'isbn':'32-987637-985345',
#         'author':'j'
#     },
#     'nodejs':
#     {
#         'isbn':'2-4357634578-59348',
#         'author':'k'
#     },
#     'mongodb':
#     {
#         'isbn':'3-8327650-87534',
#         'author':'l'
#     },
#     'vuejs':
#     {
#         'isbn':'2-43875-59834567',
#         'author':'m'
#     },
# }

