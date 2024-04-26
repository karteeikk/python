class library:
    def __init__(self):
        self.books = []
        self.book_count = 0
    def add_book(self,*book):
        self.books.append(book)
        self.book_count=len(self.books)
    def show(self):
        print(f"book  size of {self.book_count} the books are ")
        for bb in self.books:
            print(bb)
a1=library()
a1.add_book("bhagvad geeta")
a1.add_book("bhagvad geeta2")
a1.add_book("bhagvad geeta1")
a1.show()

