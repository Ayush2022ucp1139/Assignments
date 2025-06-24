class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow_book(self):
        if self.available:
            self.available = False
            return f"'{self.title}' has been borrowed."
        return f"'{self.title}' is currently unavailable."
    
    def return_book(self):
        if not self.available:
            self.available = True
            return f"'{self.title}' has been returned."
        return f"'{self.title}' was not borrowed."
    
    def check_availability(self):
        status = "available" if self.available else "unavailable"
        return f"'{self.title}' by {self.author} is {status}."
    
    def __str__(self):
        return f"Book: {self.title} | Author: {self.author} | Available: {self.available}"


# Example usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    
    print(book1.check_availability())
    print(book1.borrow_book())
    print(book1.borrow_book())
    print(book1.return_book())
    print(book1.check_availability())
    
    print("\nAll books:")
    print(book1)
    print(book2)