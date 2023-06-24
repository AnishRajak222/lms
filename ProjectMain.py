from ProjectLibrary import Library
mylibrary= Library()
mylibrary.fechBookData()
mylibrary.fechLenderData()
print("Enter the name and code of the book example: JAVA-20 ")
print("Enter your name and classroll example: Firstname Lastname-rollnumber ")
while(True):
    print(f"Enter your choice to continue")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    print("5. Delete a Book")
    print("6. To exit")
    user_choice = input()
    if user_choice not in ['1','2','3','4','5','6']:
        print("Please enter a valid option")
        continue

    else:
        user_choice = int(user_choice)

    if user_choice == 1:
        mylibrary.displayBooks()

    elif user_choice == 2:
        book = input("Enter the name of the book you want to lend: ")
        user = input("Enter your name: ")
        mylibrary.lendBook(user, book)

    elif user_choice == 3:
        book = input("Enter the name of the book you want to add: ")
        mylibrary.addBook(book)

    elif user_choice == 4:
        book = input("Enter the name of the book you want to return: ")
        ab=mylibrary.returnBook(book)
        if ab==1:
           mylibrary.lateFine(book) 
    elif user_choice == 5:
        book = input("Enter the name of the book you want to delete: ")
        mylibrary.deleteBook(book)
    elif user_choice == 6: # PLEASE EXIT BY ENTERING 6 ELSE CURRENT LENDER DATA AND BOOK DATA WILL NOT BE UPDATED !
        mylibrary.closeLibraryData()
        mylibrary.lenderData()
        mylibrary.BookData()
        break
    else:
        print("Not a valid option")  