from datetime import datetime
class Book:
    def __init__(self,author,title,availability):
        self.author = author
        self.title = title
        self.availability = True

class User:
    def __init__(self,name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions= []

    def add_books(self,title,author):
        book = Book(author,title,True) # making object for the Book class
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def display_books(self):
        print("Available Books")
        for book in self.books:
            if book.availability:
                print(f"Title: {book.title}, Author: {book.author}")

    def add_user(self,name):
        user = User(name) # making object for the User class
        self.users.append(user)
        print(f"User '{name}' registered.")

    def display_user(self):
        print("Registered Users:")
        for user in self.users:
            print(f"Name: {user.name}")

    def check_out_book(self, user_name, book_title):
        # Find the user with the given name in the list of users
        user = next((u for u in self.users if u.name == user_name), None)
        # Find the book with the given title that is available for checkout
        book = next((b for b in self.books if b.title == book_title and b.available), None)
        # Check if both user and book are found
        if user and book:
            # Set the book's availability to False, indicating it is checked out
            book.available = False
            # Record the transaction details (user, book, and current date)
            transaction = {"user": user.name, "book": book.title, "date": str(datetime.datetime.now())}
            self.transactions.append(transaction)
            # Print a success message
            print(f"Book '{book.title}' checked out by {user.name}.")
        else:
            # Print a message indicating why the checkout failed
            print("User or book not found or book not available.")


def main():
        library = Library()
        while True:
              welcome_msg = '''\n ====== Welcome to Library Management System =====
              1. Add Books
              2. Display Books
              3. Add Users
              4. Display Users
              5. Check Out Books
              6. Exit
              '''
              print(welcome_msg)
              c = int(input("Enter your choice: "))
              if c == 1:
                  author = input("Enter author name: ")
                  title = input("Enter book title: ")
                  library.add_books(author,title)
              elif c == 2:
                  library.display_books()
              elif c == 3:
                  name = input("Enter name of the user: ")
                  library.add_user(name)
              elif c==  4:
                  library.display_user()
              elif c == 5:
                  user_name = input("Enter the name of the user: ")
                  book_title = input("Enter the title of the book to check out: ")
                  library.check_out_book(user_name, book_title)
              elif c == 6:
                  print("Exiting the program,Thankyou!")
                  exit()
              else:
                  print('Invalid choice. Please try again!')
if __name__ == '__main__':
    main()




