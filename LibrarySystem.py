# Imports
import sys


class Library:  # Initialise class Library.
    def __init__(self):  # Initialise constructor.
        self.books = []  # Set self.books to [] empty list.]
        self.borrowed_books = []

    def display_books(self):
        return self.books  # Display Books

    def add_book(self, book):
        self.books.append(book)  # Append instances to book

    def edit_book(self, key_value, value_to_replace, replaced_value):
        for i in self.books:  # Loops through the list of dictionaries.
            if i[key_value] == value_to_replace:  # i[key_value] such as ID. == value of the ID.
                i[key_value] = replaced_value  # The value to replace
                break  # only allows run once.

    def borrow_book(self, key_value, value):
        for i in self.books[:]:   # Loops through individual dictionaries.
            if i[key_value] == value:  # i[key_value] such as ID. Value of the ID, remove whole dictionary.
                self.borrowed_books.append(i)  # borrows dictionary to borrowed books empty list.
                self.books.remove(i)
                break

    def buy_book(self, key_value, value):
        for i in self.books[:]:  # Loops through individual dictionaries.
            if i[key_value] == value:  # i[key_value] such as ID. Value of the ID, remove whole dictionary.
                self.books.remove(i)  # Removes dictionary / buys book
                break  # Only allows run once.

    def search(self, key, value):
        return [x for x in self.books if x[key] == value]

    def sort_book(self, key_value):
        self.books.sort(key=lambda d: d[key_value])

    def display_borrowed_books(self):
        return self.borrowed_books

    def return_borrowed_book(self, key_value, value):
        for i in self.borrowed_books[:]:
            if i[key_value] == value:
                self.books.append(i)
                self.borrowed_books.remove(i)
                break


class Book:
    def __init__(self):
        self.unique_id = None
        self.book_id = None
        self.unique_title_id = None
        self.book_title = None
        self.unique_author_id = None
        self.book_author = None
        self.unique_year_id = None
        self.book_year = None

    def set_unique_id_key(self):
        self.unique_id = 'ID'  # Sets the unique_ID

    def set_value_for_id(self):
        self.book_id = input("ID = ")  # Sets the value for ID

    def set_unique_title_id(self):
        self.unique_title_id = 'Title'  # Sets the unique_Title

    def set_value_for_title(self):
        self.book_title = input("Title = ")  # Sets the value for Title

    def set_unique_author_key(self):
        self.unique_author_id = 'Author'  # Sets the unique_Author

    def set_value_for_author(self):
        self.book_author = input("Author = ")  # Sets the value for Author

    def set_unique_year_id(self):
        self.unique_year_id = 'Year'  # Sets the unique_Year

    def set_value_for_year(self):
        self.book_year = input("Year of publication = ")  # Sets the value for Year

    def to_dict(self):
        #  Returns all the set keys and values.
        return {self.unique_id: self.book_id, self.unique_title_id: self.book_title,
                self.unique_author_id: self.book_author, self.unique_year_id: self.book_year}


class Student:
    def __init__(self):
        self.book = input("Enter the key value: ")

    def request_book(self):
        return self.book


def main():
    flag = False
    while flag is False:
        print("""========LIBRARY MENU========
                1. Display Books
                2. Add Books
                3. Edit Book
                4. Borrow book
                5. Buy books
                6. Search for book
                7. Sort books
                8. Display borrowed books
                9. Return borrowed books
                10. Exit""")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            for x in library.display_books():
                print(x)
        elif choice == 2:
            # Calls Book methods to add books to the system.
            books.set_unique_id_key()
            books.set_value_for_id()
            books.set_unique_title_id()
            books.set_value_for_title()
            books.set_unique_author_key()
            books.set_value_for_author()
            books.set_unique_year_id()
            books.set_value_for_year()
            the_dict = books.to_dict()
            library.add_book(the_dict)  # creates multiple dictionaries
        elif choice == 3:
            library.edit_book(input("Enter the key value to edit: "), input("Enter the value you want to replace: "),
                              input("Enter a new value: "))
        elif choice == 4:
            library.borrow_book(input("Enter key value: "), input("Enter the value to borrow: "))
        elif choice == 5:
            student = Student()
            library.buy_book(student.request_book(), input("Enter the value to remove: "))
        elif choice == 6:
            print(library.search(input("Enter the key: "), input("Enter the value: ")))
        elif choice == 7:
            library.sort_book(input("Enter the key value to sort: "))
        elif choice == 8:
            for x in library.display_borrowed_books():
                print(x)
        elif choice == 9:
            library.return_borrowed_book(input("Enter the key value: "), input("Enter the value to remove: "))
        elif choice == 10:
            sys.exit()


books = Book()
library = Library()  # Set library to Library() class.

# Test data
library.add_book({'ID': '1', 'Title': 'Algorithms', 'Author': 'Chang', 'Year': '2008'})
library.add_book({'ID': '3', 'Title': 'Computer science fundamentals', 'Author': 'Jk', 'Year': '2017'})
library.add_book({'ID': '6', 'Title': 'Networking', 'Author': 'Abba', 'Year': '2008'})
library.add_book({'ID': '4', 'Title': 'Security', 'Author': 'Tia', 'Year': '2019'})
library.add_book({'ID': '5', 'Title': 'Machine learning neural networks', 'Author': 'Seat', 'Year': '2020'})
library.add_book({'ID': '2', 'Title': 'Web development', 'Author': 'Weller', 'Year': '2005'})
library.add_book({'ID': '7', 'Title': 'Data structures', 'Author': 'Harp', 'Year': '1993'})
library.add_book({'ID': '8', 'Title': 'Automating the boring stuff with python', 'Author': 'Red', 'Year': '1987'})
library.add_book({'ID': '9', 'Title': 'Data model', 'Author': 'Alexander', 'Year': '2006'})


main()

