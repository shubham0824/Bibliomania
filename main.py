from library_class import Library
from Credentials import credential
username, password = credential()
          



if __name__ == '__main__':

    l1 = Library("Shubham's library")

    while True:
        print(f"\n Welcome to the {l1.library_name}.\n")
        print("Press :-")
        option = int(input("1. Search a book in the library\n"
                       "2. Borrow a book from Library\n"
                       "3. Return a borrowed book\n"
                       "4. Quit\n"
                       "5. See the list of books borrowed and by whom(Only for Admin)\n"
                       ">>> ").rstrip())

        if option == 1:
            while True:
                user_input = int(input("Press:- \n"
                                    "1. Search by book title\n"
                                    "2. Search by ISBN number\n"
                                    "3. Search by author name\n"))
                if user_input == 1:
                    book_title = input("Enter the book title to Search: ").capitalize().rstrip()
                    print("\n")
                    l1.searchbookbytitle(book_title)
                    break
                elif user_input == 2:
                    isbn_number = input("Enter the ISBN number to Search: ").rstrip()
                    print('\n')
                    l1.searchbookbyisbn(isbn_number)
                    break
                elif user_input == 3:
                    author_name = input("Enter the author name to Search: ").rstrip()
                    print('\n')
                    l1.searchbookbyauthor(author_name)
                    break
                else:
                    option = input("Invalid Input: Want to retry press 'y' else press any key: ")
                    if option == 'y':
                        continue
                    else:
                        break

        elif option == 2:
            client_name = input("Please Provide your Full name: ").capitalize()
            book_name = input("Which book you want to Lend: ").capitalize().rstrip()
            l1.borrowbooks(client_name.lower(),book_name)

        elif option == 3:
            client_name = input("Please Provide your Full name: ")
            book_name = input("Which book you want to Return: ").capitalize().rstrip()
            l1.returnbook(client_name.lower(),book_name)


        elif option == 4:
            exit()


        elif option == 5:            
             while True:
                username_by_user = input("Enter Your User Name: ")
                password_by_user = input("Enter Your Paasword: ")
                if username_by_user == username and password_by_user == password:
                    l1.borrowedbooklist()
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
