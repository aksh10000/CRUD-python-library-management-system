#import all the necessary libraries including book,magazine,user and transactions classes from models
import json
#import typing for type checking and error handling
from typing import List, Dict, Any, TypeVar, Generic, Generator
from models import Book, Magazine, User, Transaction
#import jsonpickle to save the custom class objects(by making them serializable) in a json file
import jsonpickle
#for defining generic class
T = TypeVar('T')
#creating a storage that will be of the following types: User, Magazine, Book, Transaction
class Storage(Generic[T]):
    #initailizing the Storage class
    def __init__(self, file_name: str):
        self.file_name = file_name
        #initializing the dictionary
        self.data: Dict[str, T] = {}
    # loading the file inside the dictionary
    def load(self) -> None:
        try:
            #opening the file
            '''
                context manager
            '''
            with open(self.file_name, 'r') as file:
                file_content = file.read() 
                #reading the json file inside the python dictionary using json decode
                self.data = jsonpickle.decode(file_content)
        #if the file is not found raise an error
        except FileNotFoundError:
            self.data = {}
    #save the updated dictionary inside the json file
    def save(self) -> None:
        with open(self.file_name, 'w') as file:
            file.write(jsonpickle.encode(self.data, indent=2))
    #add a new item to the dictionary and save the updated dictionary to the json file
    def add(self, key: str, item: T) -> None:
        self.data[key] = item
        self.save()
    #get a particular item based on the key value
    def get(self, key: str) -> T:
        return self.data.get(key)
    #update a particular item based on key value
    def update(self, key: str, item: T) -> None:
        if key in self.data:
            self.data[key] = item
            self.save()
    #delete a particular item based on a particular key
    def delete(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
            self.save()
    #list all the items
    def list_all(self):
        '''
            Generator Expression
        '''
        return (value for value in self.data.values())
#initialize the book storage by inheriting the storage class
class BookStorage(Storage[Book]):
    def __init__(self):
        #initialize the parent class
        super().__init__('books.json')
    #search for a particular book on the basis of title, author or isbn
    def search(self, query: str) -> List[Book]:
        return [book for book in self.data.values() if
                query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query.lower() in book.isbn.lower()]
#initialize the magazine storage by inheriting the storage class 
class MagazineStorage(Storage[Magazine]):
    def __init__(self):
        #initialize the parent constructor
        super().__init__('magazines.json')
    #search for a particular magazine on the basis of title, issue_number or publisher
    def search(self, query: str) -> List[Magazine]:
        return [magazine for magazine in self.data.values() if
                query.lower() in magazine.title.lower() or
                query.lower() in magazine.issue_number.lower() or
                query.lower() in magazine.publisher.lower()]
#initialize the user storage
class UserStorage(Storage[User]):
    def __init__(self):
        #initialize the parent constructor
        super().__init__('users.json')
    #search for a particular user on the basis of name, user_id or email
    def search(self, query: str) -> List[User]:
        return [user for user in self.data.values() if
                query.lower() in user.name.lower() or
                query.lower() in user.user_id.lower() or
                query.lower() in user.email.lower()
                ]
#initalize the transaction manager
class TransactionStorage(Storage[Transaction]):
    def __init__(self):
        #initialize the parent constructor
        super().__init__('transactions.json')
    #add a transaction
    def add_transaction(self, transaction: Transaction) -> None:
        self.data[str(len(self.data))] = transaction
        self.save()