#import menu driver cli control
from cli import CLI

def main():
    #create an instance of the menu driven cli control library management system
    print("Welcome to the Library Management System")
    cli = CLI()
    #run the library management system
    cli.run()

if __name__ == "__main__":
    main()