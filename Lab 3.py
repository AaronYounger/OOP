## Book_class (book_id, book_title, author_id, publisher, year_of_publication)
## Author_class (author_id, author_name, affiliation, country, phone, email_id)
## User_class (user_id, name, password, address, phone, email_id, booksborroowed=[]

class Book:
    def __init__(self, book_id, book_title, author_id, publisher, year_of_publication):
        self.book_id = book_id
        self.book_title = book_title
        self.author_id = author_id
        self.publisher = publisher
        self.year_of_publication = year_of_publication

    def display_books(self):
        print("Book Title:", self.book_title)
        print("Publisher:", self.publisher)
        print("Year Of Publication: ", self.year_of_publication)

    def display_book_title(self):
        print("Book Title:", self.book_title)

class Author:
    def __init__(self, author_id, author_name, affiliation, country, phone, email_id):
        self.author_id = author_id
        self.author_name = author_name
        self.affiliation = affiliation
        self.country = country
        self.phone = phone
        self.email_id = email_id
    def display_author(self):
        print("Author Name:", self.author_name)
        print("Author Affiliation:", self.affiliation)
        print("Authors Country:", self.country)
        print("Authors Phone: ", self.phone)
class User:
    def __init__(self, user_id, email_id):
        self.user_id = user_id
        self.name = ""
        self.password = 0.0
        self.address = ""
        self.email_id = email_id
        self.booksborrowed = []

    def add_user(self):
        self.name = input("Enter Your Name: ")
        self.password = int(input("Enter Numerical Password: "))
        self.address = input("Enter your Address: ")

    def display_user(self):
        print("User Name:", self.name)
        print("User Password:", self.password)
        print("User Address:", self.address)

    def display_user_book(self):
        for x in self.booksborrowed:
            print("Title of Borrowed Book:", x.book_title)

    def borrowed_book(self, bk):
        self.booksborrowed.append(bk)

    def return_book(self, bk):
        self.booksborrowed.remove(bk)

book1 = Book(1, "Around the World in Eighty Days", "101", "Jules Verne", "1950")
book2 = Book(2, "Old Man in the Sea", "104", "Earnest Hemingway", "1952")
book3 = Book(3, "Fahrenheit 451", "110", "Ray Bradbury", "1960")

author1 = Author(1, "Jules Verne", "French Novelist", "France", "111-111-1111", "1")
author2 = Author(2, "Earnest Hemingway", "American author", "American", "222-222-2222", "2")
author3 = Author(3, "Ray Bradbury", "American Author", "American", "333-333-3333", "3")

User1 = User(1, "1")
User2 = User(2, "2")
User3 = User(3, "3")

allusers = []

while True:
    print("1. Put In Your Information")
    print("2. Display User Information")
    print("3. See Available Books")
    print("4. See Author Information of Available Books")
    print("5. Borrow A Book")
    print("6. Print Books You Have Borrowed")
    print("7. Return Books Borrowed")

    options = int(input("Select Action: "))

    if options == 1:
            User1.add_user()
            allusers.append(User1)

    elif options == 2:
        User1.display_user()

    elif options == 3:
        book1.display_books()
        book2.display_books()
        book3.display_books()

    elif options == 4:
        author1.display_author()
        author2.display_author()
        author3.display_author()

    elif options == 5:
        while True:
            print("1. Borrow Around the World in Eighty Days")
            print("2. Borrow Old Man in the Sea")
            print("3. Borrow Fahrenheit 451")

            options1 = int(input("Enter What Book You Want to Borrow: "))

            if options1 == 1:
                User1.borrowed_book(book1)
                break

            if options1 == 2:
                User1.borrowed_book(book2)
                break

            if options1 == 3:
                User1.borrowed_book(book3)
                break
    elif options == 6:
        User1.display_user_book()

    elif options == 7:
        while True:
            print("1. Return Around the World in Eighty Days")
            print("2. Return Old Man in the Sea")
            print("3. Return Fahrenheit 451")

            User1.display_user_book()
            options2 = int(input("Enter Book you want to Return: "))

            if options2 == 1:
                User1.return_book(book1)
                break
            if options2 == 2:
                User1.return_book(book2)
                break
            if options2 == 3:
                User1.return_book(book3)
                break



