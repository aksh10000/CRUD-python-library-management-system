#import the abstract class base and abstract class methods
from abc import ABC, abstractmethod
#for logging the timestamp
from datetime import datetime
#for type checking and error handling
from typing import List, Optional, Dict
#set the abstract class base using ABC, necessary to define the abstract functions
class Item(ABC):
    #initialize the instructor
    def __init__(self, item_id: str, title: str):
        self._item_id = item_id
        self._title = title
        self._is_available = True
    #property decorator to enable functions usable as if they were parameters 
    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def is_available(self) -> bool:
        return self._is_available

    def set_availability(self, status: bool) -> None:
        self._is_available = status
    #abstract method which must be implemented by child class
    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass

class Book(Item):
    #initialize the child and parent class constructor
    def __init__(self, item_id: str, title: str, author: str, isbn: str):
        super().__init__(item_id, title)
        self._author = author
        self._isbn = isbn
    #property decorator to enable functions usable as if they were parameters 
    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn
    #defining the abstract methods here
    def get_info(self) -> str:
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn}) Availibility: {self.is_available}"
    #defining the abstract methods here
    def get_type(self) -> str:
        return "Book"

class Magazine(Item):
    def __init__(self, item_id: str, title: str, issue_number: str, publisher: str):
        #initialize the child and parent class constructor
        super().__init__(item_id, title)
        self._issue_number = issue_number
        self._publisher = publisher
    #property decorator to enable functions usable as if they were parameters 
    @property
    def issue_number(self) -> str:
        return self._issue_number
    #property decorator to enable functions usable as if they were parameters 
    @property
    def publisher(self) -> str:
        return self._publisher
    #defining the abstract methods here
    def get_info(self) -> str:
        return f"Magazine: {self.title}, Issue {self.issue_number} by {self.publisher}"
    #defining the abstract methods here
    def get_type(self) -> str:
        return "Magazine"

class User:
    #initialize the constructor
    def __init__(self, user_id: str, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._borrowed_items: Dict[str,Item] = {}
    #property decorator to enable functions usable as if they were parameters 
    @property
    def user_id(self) -> str:
        return self._user_id
    #property decorator to enable functions usable as if they were parameters 
    @property
    def name(self) -> str:
        return self._name
    #property decorator to enable functions usable as if they were parameters 
    @property
    def email(self) -> str:
        return self._email
    #property decorator to enable functions usable as if they were parameters 
    @property
    def borrowed_items(self) -> Dict[str,Item]:
        return self._borrowed_items.copy()

    def borrow_item(self, item: Item) -> None:
        if item.is_available:
            self._borrowed_items[item.item_id]=item
            item.set_availability(False)
        else:
            print(f'{item.title} is not available')

    def return_item(self, item: Item) -> None:
        if item.item_id in self._borrowed_items.keys():
            del self._borrowed_items[item.item_id]
            item.set_availability(True)
        else:
            print(f"{item.title} was not borrowed, so it can not be returned")

class Transaction:
    #initialize the constructor
    def __init__(self, user: User, item: Item, transaction_type: str):
        self._user = user
        self._item = item
        self._transaction_type = transaction_type
        self._timestamp = datetime.now()
    #property decorator to enable functions usable as if they were parameters 
    @property
    def user(self) -> User:
        return self._user
    #property decorator to enable functions usable as if they were parameters 
    @property
    def item(self) -> Item:
        return self._item
    #property decorator to enable functions usable as if they were parameters 
    @property
    def transaction_type(self) -> str:
        return self._transaction_type
    #property decorator to enable functions usable as if they were parameters 
    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def get_info(self) -> str:
        return f"{self.transaction_type}: {self.user.name}(User) - {self.item.title} ({self.item.get_type()}) at {self.timestamp}"