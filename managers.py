#import typing for type checking and error identification
from typing import List, Optional, Type, Generator
#import the model blueprints
from models import Book, Magazine, User, Transaction, Item
#import the different kinds of storages
from storage import Storage, BookStorage, MagazineStorage, UserStorage, TransactionStorage

#defining error handling classes
class LibraryException(Exception):
    '''
        Used to handle exceptions
    '''
    pass
#inheriting LibraryException inside ItemNotFoundError class
class ItemNotFoundError(LibraryException):
    '''Used to handle item not found exception'''
    pass
#inheriting LibraryException inside ItemNotAvailableError class
class ItemNotAvailableError(LibraryException):
    '''Used to handle item not available exception'''
    pass

#generic ItemManager class that is inherited by BookManager and MagazineManager classes
class ItemManager:
    '''Used as a parent class by Magazine manager and Book managernclasses'''
    #instructor for initializing, item will be either 'Book' or 'Magazine' class and storage will either be book storage or magazine storage
    def __init__(self, item_class: Type[Item], storage_class: Type[Storage]):
        self.item_class = item_class
        self.storage = storage_class()
        self.storage.load()
    #for adding an item
    def add_item(self, item: Item) -> None:
        #if item is already exists with a particular id raise an ItemNotFoundError otherwise add the item
        if self.storage.get(item.item_id):
            raise LibraryException(f"{self.item_class.__name__} with ID {item.item_id} already exists")
        self.storage.add(item.item_id, item)
    #for updating the details a prexisting item
    def update_item(self, item: Item) -> None:
        #if item is not found raise an ItemNotFoundError otherwise update the item
        if not self.storage.get(item.item_id):
            raise ItemNotFoundError(f"{self.item_class.__name__} with ID {item.item_id} not found")
        self.storage.update(item.item_id, item)
    #for deleting an item
    def delete_item(self, item_id: str) -> None:
        #if item is not found raise an ItemNotFoundError otherwise delete the item
        if not self.storage.get(item_id):
            raise ItemNotFoundError(f"{self.item_class.__name__} with ID {item_id} not found")
        self.storage.delete(item_id)
    #for getting an item
    def get_item(self, item_id: str) -> Item:
        #get the item on the basis of item id
        item = self.storage.get(item_id)
        #if item is not found i.e. item is 'None' raise an ItemNotFoundError otherwise return the item
        if not item:
            raise ItemNotFoundError(f"{self.item_class.__name__} with ID {item_id} not found")
        return item
    #for listing all the items
    def list_items(self):
        return self.storage.list_all()
    #for searching an item
    def search_items(self, query: str) -> List[Item]:
        return self.storage.search(query)
#inherits item manager class
class BookManager(ItemManager):
    
    def __init__(self):
        #initializing parent class
        super().__init__(Book, BookStorage)
#inherites item manager class
class MagazineManager(ItemManager):
    def __init__(self):
        #initializing parent class
        super().__init__(Magazine, MagazineStorage)

#manages the user storage
class UserManager:
    '''Used to implement User manager that is going to manage the users'''
    def __init__(self):
        #initializing an instance of UserStorage class
        self.storage = UserStorage()
        #loading the dictionary from the json file
        self.storage.load()
    #adding a user
    def add_user(self, user: User) -> None:
        #if user already exists raise an error otherwise just add the new user
        if self.storage.get(user.user_id):
            raise LibraryException(f"User with ID {user.user_id} already exists")
        self.storage.add(user.user_id, user)

    def update_user(self, user: User) -> None:
        #if user does not exist raise an error otherwise just update the user
        if not self.storage.get(user.user_id):
            raise ItemNotFoundError(f"User with ID {user.user_id} not found")
        self.storage.update(user.user_id, user)

    def delete_user(self, user_id: str) -> None:
        #if user does not exist raise an error otherwise delete the user
        if not self.storage.get(user_id):
            raise ItemNotFoundError(f"User with ID {user_id} not found")
        self.storage.delete(user_id)

    def get_user(self, user_id: str) -> User:
        #if the user doesn't exist raise an error otherwise return the user
        user = self.storage.get(user_id)
        if not user:
            raise ItemNotFoundError(f"User with ID {user_id} not found")
        return user

    def list_users(self):
        #list the users
        return self.storage.list_all()

    def search_users(self, query: str) -> List[User]:
        #search for a particular user using name, email or user id
        return self.storage.search(query)
#transaction manager class
class TransactionManager:
    '''Used for management of transactions'''
    def __init__(self):
        #initialize the transaction manager
        self.storage = TransactionStorage()
        #load the dictionary from the json file
        self.storage.load()

    def add_transaction(self, transaction: Transaction) -> None:
        #add a transaction to the storage
        self.storage.add_transaction(transaction)

    def list_transactions(self):
        #return the list of transactions
        return self.storage.list_all()

class LibraryManager:
    '''Used for management of users, magazines, books and transactions'''
    #intialize the library manager
    def __init__(self):
        #initialize different managers for using library manager
        self.book_manager = BookManager()
        self.magazine_manager = MagazineManager()
        self.user_manager = UserManager()
        self.transaction_manager = TransactionManager()
    #check out an item i.e. a book or magazine
    def checkout_item(self, user_id: str, item_id: str) -> None:
        #get the user id and item id
        try:
            user = self.user_manager.get_user(user_id)
            item = self.get_item(item_id)
        except ItemNotFoundError as e:
            #if the user id and item id are not found raise an error
            raise LibraryException(str(e))
        #check if the item is not avialable, if it is not available raise an error
        if not item.is_available:
            raise ItemNotAvailableError(f"{item.get_type()} with ID {item_id} is not available for checkout")
        #add the borrowed book or magazine to the borrowed item dictionary of the user
        user.borrow_item(item)
        #update the details of the user in the user manager
        self.user_manager.update_user(user)
        #update the item
        self.update_item(item)
        #create a new transaction
        transaction = Transaction(user, item, "Checkout")
        #save the transaction in the new transaction manager
        self.transaction_manager.add_transaction(transaction)
    #checkin an item
    def checkin_item(self, user_id: str, item_id: str) -> None:
        #get the user id and item id
        try:
            user = self.user_manager.get_user(user_id)
            item = self.get_item(item_id)
        except ItemNotFoundError as e:
            #if item id or user id is not found raise an error
            raise LibraryException(str(e))
        #get the item ids that are borrowed by the user
        borrowed_item_ids = list(user.borrowed_items.keys())
        #if the current item's id does not exist in the user borrowed items ids then raise an error that the item was not borrowed by the user
        if item.item_id not in borrowed_item_ids:
            raise LibraryException(f"{item.get_type()} with ID {item_id} is not borrowed by user with ID {user_id}")
        #return the item
        user.return_item(item)
        #update the user details
        self.user_manager.update_user(user)
        #update teh detials of the item
        self.update_item(item)
        #create a transaction
        transaction = Transaction(user, item, "Checkin")
        #add the transaction to the transaction manager
        self.transaction_manager.add_transaction(transaction)
    #get an item
    def get_item(self, item_id: str) -> Item:
        try:
            #return the book
            return self.book_manager.get_item(item_id)
        #otherwise return the magazine
        except ItemNotFoundError:
            return self.magazine_manager.get_item(item_id)

    def update_item(self, item: Item) -> None:
        #check if the item is an instance of book, if so update the book
        if isinstance(item, Book):
            self.book_manager.update_item(item)
        #check if the item is an instance of the magazine, if so update the magazine
        elif isinstance(item, Magazine):
            self.magazine_manager.update_item(item)
        else:
            #otherwise raise an error
            raise LibraryException(f"Unknown item type: {type(item)}")
