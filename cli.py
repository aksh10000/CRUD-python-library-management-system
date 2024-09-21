#import uuid for generatin unique strings that can be used as unique ids
import uuid
#import the managers
from managers import LibraryManager,LibraryException,ItemNotFoundError,ItemNotAvailableError
#import the models
from models import Book, User, Magazine

class CLI:
    '''
        cli class is implemented to initialize the library management class and interact with it
    '''
    def __init__(self):
        #initialize the library manager
        self.library_manager = LibraryManager()

    def run(self):
        while True:
            #display the menu and handle the choice
            self.display_menu()
            choice = input("Enter your choice: ")
            self.handle_choice(choice)

    def display_menu(self):
        #call different functions based on different inputs
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Add User")
        print("7. Update User")
        print("8. Delete User")
        print("9. List Users")
        print("10. Search Users")
        print("11. Checkout Book")
        print("12. Checkin Book")
        print("13. Add Magazine")
        print("14. Update Magazine")
        print("15. Delete Magazine")
        print("16. List Magazines")
        print("17. Search Magazines")
        print("18. Checkout Magazine")
        print("19. Checkin Magazine")
        print("20. List Transactions")
        print("0. Exit")
    #define the choice handling logic
    def handle_choice(self, choice):
        if choice == "1":
            self.add_book()
        elif choice == "2":
            self.update_book()
        elif choice == "3":
            self.delete_book()
        elif choice == "4":
            self.list_books()
        elif choice == "5":
            self.search_books()
        elif choice == "6":
            self.add_user()
        elif choice == "7":
            self.update_user()
        elif choice == "8":
            self.delete_user()
        elif choice == "9":
            self.list_users()
        elif choice == "10":
            self.search_users()
        elif choice == "11":
            self.checkout_book()
        elif choice == "12":
            self.checkin_book()
        elif choice == "13":
            self.add_magazine()
        elif choice == "14":
            self.update_magazine()
        elif choice == "15":
            self.delete_magazine()
        elif choice == "16":
            self.list_magazine()
        elif choice == "17":
            self.search_magazines()
        elif choice == "18":
            self.checkout_magazine()
        elif choice == "19":
            self.checkin_magazine()
        elif choice == "20":
            self.list_transactions()
        elif choice == "0":
            print("Thank you for using the Library Management System. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
    #to add a book
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        #create a unique id for the book
        book_id = str(uuid.uuid4())
        book = Book(book_id, title, author, isbn)
        self.library_manager.book_manager.add_item(book)
        print(f"Book added successfully. Book ID: {book_id}")
    #to update a book
    def update_book(self):
        book_id = input("Enter book ID to update: ")
        book = self.library_manager.book_manager.get_item(book_id)
        if book:
            title = input(f"Enter new title (current: {book.title}): ") or book.title
            author = input(f"Enter new author (current: {book.author}): ") or book.author
            isbn = input(f"Enter new ISBN (current: {book.isbn}): ") or book.isbn
            updated_book = Book(book_id, title, author, isbn)
            #save updated book at the place of original book
            self.library_manager.book_manager.update_item(updated_book)
            print("Book updated successfully.")
        else:
            print("Book not found.")
    #to delete a book
    def delete_book(self):
        book_id = input("Enter book ID to delete: ")
        book = self.library_manager.book_manager.get_item(book_id)
        if book:
            self.library_manager.book_manager.delete_item(book_id)
            print("Book deleted successfully.")
        else:
            print("Book does not exist")
    #to list all the books
    # it receives a python generator expression for lazy loading
    def list_books(self):
        #books receives a generator expression
        books = self.library_manager.book_manager.list_items()
        # print(books)
        if books == 0:
            print("No books exist")
        else:
            for item in books:
                book = item
                print(book.get_info())

    def search_books(self):
        #to search for a book
        query = input("Enter search query: ")
        books = self.library_manager.book_manager.search_items(query)
        if len(books) == 0:
            print("No such books exist")
        else:
            for book in books:
                print(book.get_info())
    # to check out a book
    def checkout_book(self):
        user_id = input("Enter user ID: ")
        book_id = input("Enter book ID: ")
        try:
            self.library_manager.checkout_item(user_id, book_id)
            print("Book checked out successfully.")
        except ItemNotAvailableError as e:
            raise LibraryException(str(e))
    #to checkin a book
    def checkin_book(self):
        user_id = input("Enter user ID: ")
        book_id = input("Enter book ID: ")
        try:
            self.library_manager.checkin_item(user_id, book_id)
            print("Book checked in successfully.")
        except ItemNotAvailableError as e:
            raise LibraryException(str(e))
    #to add a magazine
    def add_magazine(self):
        title = input("Enter Magazine title: ")
        issue_number = input("Enter Magazine issue number: ")
        publisher = input("Enter the publisher: ")
        #create a unique id for the magazine
        magazine_id = str(uuid.uuid4())
        #create a magazine
        magazine = Magazine(magazine_id, title, issue_number, publisher)
        self.library_manager.magazine_manager.add_item(magazine)
        print(f"Magazine added successfully. Magazine ID: {magazine_id}")
    #to update a magazine
    def update_magazine(self):
        magazine_id = input("Enter magazine ID to update: ")
        magazine = self.library_manager.magazine_manager.get_item(magazine_id)
        if magazine:
            title = input(f"Enter new title (current: {magazine.title}): ") or magazine.title
            issue_number = input(f"Enter new magazine issue number (current: {magazine.issue_number}): ") or magazine.issue_number
            publisher = input(f"Enter new publisher (current: {magazine.publisher}): ") or magazine.publisher
            updated_magazine = Magazine(magazine_id, title, issue_number, publisher)
            self.library_manager.magazine_manager.update_item(updated_magazine)
            print("Megazine updated successfully.")
        else:
            print("Megazine not found.")
    #to delete a magazine
    def delete_magazine(self):
        magazine_id = input("Enter magazine ID to delete: ")
        magazine = self.library_manager.magazine_manager.get_item(magazine_id)
        if magazine:
            self.library_manager.magazine_manager.delete_item(magazine_id)
            print("Magazine deleted successfully.")
        else:
            print("Magazine does not exist")
    #to list all the magazines
    #receives a python generator expression
    def list_magazine(self):
        magazines = self.library_manager.magazine_manager.list_items()
        for item in magazines:
            magazine = item 
            print(magazine.get_info())
    #search for a particular magazine
    def search_magazines(self):
        query = input("Enter search query: ")
        magazines = self.library_manager.magazine_manager.search_items(query)
        if len(magazines) == 0:
            print("No such magazines exist")
        else:
            for magazine in magazines:
                print(magazine.get_info())
    #check out a magazine
    def checkout_magazine(self):
        user_id = input("Enter user ID: ")
        magazine_id = input("Enter magazine ID: ")
        try:
            self.library_manager.checkout_item(user_id, magazine_id)
            print("Magazine checked out successfully.")
        except ItemNotAvailableError as e:
            raise LibraryException(str(e))
    #checkin a magazine
    def checkin_magazine(self):
        user_id = input("Enter user ID: ")
        magazine_id = input("Enter magazine ID: ")
        try:
            self.library_manager.checkin_item(user_id, magazine_id)
            print("Magazine checked in successfully.")
        except ItemNotAvailableError as e:
            raise LibraryException(str(e))
    #add a user
    def add_user(self):
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email)
        self.library_manager.user_manager.add_user(user)
        print(f"User added successfully. User ID: {user_id}")
    #update a user
    def update_user(self):
        user_id = input("Enter user ID to update: ")
        user = self.library_manager.user_manager.get_user(user_id)
        if user:
            name = input(f"Enter new name (current: {user.name}): ") or user.name
            email = input(f"Enter new email (current: {user.email}): ") or user.email
            updated_user = User(user_id, name, email)
            self.library_manager.user_manager.update_user(updated_user)
            print("User updated successfully.")
        else:
            print("User not found.")
    #delete a user
    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        self.library_manager.user_manager.delete_user(user_id)
        print("User deleted successfully.")
    #list all the users
    def list_users(self):
        users = self.library_manager.user_manager.list_users()
        for user in users:
            print(f"User ID: {user.user_id}, Name: {user.name}, Email: {user.email}")
    #search for a particular user
    def search_users(self):
        query = input("Enter search query: ")
        users = self.library_manager.user_manager.search_users(query)
        if len(users) == 0:
            print("No such user exists")
        else:
            for user in users:
                print(f"User ID: {user.user_id}, Name: {user.name}, Email: {user.email}")

    
    #to list all the transactions
    #receives a python genertor object
    def list_transactions(self):
        transactions = self.library_manager.transaction_manager.list_transactions()
        for transaction in transactions:
            print(transaction.get_info())
