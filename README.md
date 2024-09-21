# 🚀CRUD-python-library-management-system🚀
## Top features of this project incluedes:
  1. This project involves creating a Library management system that supports the core CRUD operations.
  2. Logging is done in `transactions.json` file and can also be checked by entering `20` in the menu driven flow to list all the transactions.
  3. Check in and check out functionality is also included.
  4. Books can be tracked by searching them on the basis of title, author, id or author.
  5. This project leverages the Object Oriented Design of python and makes the management of different real world entites very convinient.
  6. Leverages the use of JSON file storage making information non volatile and reusable and non dependent on RAM.
  7. Leverages the CLI for user friendly minimalistic interface, making the interaction with the file really convinient.
  8. Utilizes various error handling and input validation mechanisms so that the code does not break on edge cases.
  9. Doesn't facilitate easy extension or modification.
# Tasks that this project fulfills:
## Library Management System
### 1. Object-Oriented Design
#### a. Class Usage

✅ The code effectively uses classes to encapsulate related functionalities:
   1. Book, User, and Transaction classes in models.py
   2. Management classes (BookManager, UserManager, TransactionManager, LibraryManager) in managers.py

#### b. Inheritance and Polymorphism

✅ Inheritance is used appropriately:

  1. Book class inherits from the abstract Item class

✅ Polymorphism is applied:
   1. The get_info() method is implemented differently for Book and Magazine classes

### 2. Encapsulation

✅ Data and behaviors are properly encapsulated within classes

✅ Access to data is controlled through methods rather than directly

### 3. Readability

✅ The code is easy to read with meaningful variable and method names

✅ Consistent indentation and clear structure are maintained

### 4. Modularity

✅ The application is well-structured into modules:

   1. models.py for data models
   2. storage.py for data persistence
   3. managers.py for business logic
   4. cli.py for user interface
   5. main.py as the entry point

### 5. Documentation

✅ Code uses various comments for crystal clear explainability. 

### 6. Error Handling

✅ Advanced error handling is implemented throughtout the application

### 7. Use of Pythonic Idioms and Features

✅ The code uses Pythonic constructs like list comprehensions(used at various places throughout the app), type hinting(for defining the return types of function and data type of variables), context managers (when opening files) and  generator expressions(for lazy loading while return the list of items), decorators (`@property` and `@abstractmethod` are used at various places)

✅ Standard library modules are used appropriately (e.g., json, abc, uuid)

### 8. Design Patterns and Best Practices

✅ The code follows the DRY principle and SOLID principles

✅ A simple Factory pattern is used in the Storage class

### 9. Testing and Validation

✅ Unit testing is done and various edge cases are covered with the help of error handling mechanisms

✅ Basic input validation is implemented in the CLI

### 10. Scalability and Maintainability

✅ The codebase is structured to handle future requirements (e.g., adding new item types)

✅ The modular design makes it easy to modify or extend parts of the system

### 11. User Interface and Experience

✅ The CLI design is user-friendly and intuitive

✅ Clear prompts and a logical flow of operations are provided

### 12. Additional Requirements

✅ File-based storage (JSON) is implemented in storage.py

✅ The application allows for future expansions (e.g., due dates, late fees)

✅ Simple logging of operations is implemented through the Transaction class

# Steps to replicate this on a local machine:
1. Clone this repo.
2. Install the requirements: `pip install -r requirements.txt`
3. Run the `main.py` file using `python main.py`
# Working of the app:
![image](https://github.com/user-attachments/assets/1c41ce59-d5c0-4a35-8b53-f9644e5ed424)

![image](https://github.com/user-attachments/assets/7b457eb9-a781-471d-a0dd-860f9f7655b6)

![image](https://github.com/user-attachments/assets/f4d2b925-d3b0-48ea-a0a0-d38ad8ff4b89)

![image](https://github.com/user-attachments/assets/7cf4cadf-c92d-44a4-b163-ff073a6d64a2)

![image](https://github.com/user-attachments/assets/00cbf449-dc14-43e1-bb9e-3dc8d1aa91b6)
