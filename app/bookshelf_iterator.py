from app.interface.iterator import Iterator
from app.model.book_shelf import BookShelf

class BookshelfIterator(Iterator):
    def __init__(self, bookshelf: BookShelf):
        self.bookshelf = bookshelf
        self.index = 0

    def has_next(self) -> bool:
        return self.index < self.bookshelf.get_length()

    def next(self):
        book = self.bookshelf.get_book_at(self.index)
        self.index += 1
        return book