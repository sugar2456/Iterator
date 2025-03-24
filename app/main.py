from app.model.book import Book
from app.model.book_shelf import BookShelf
from app.bookshelf_iterator import BookshelfIterator

bookshelf: BookShelf = BookShelf(4)
bookshelf.append_book(Book("Around the World in 80 Days"))
bookshelf.append_book(Book("Bible"))
bookshelf.append_book(Book("Cinderella"))
bookshelf.append_book(Book("Daddy-Long-Legs"))

it: BookshelfIterator = bookshelf.iterator()
while it.has_next():
    book: Book = it.next()
    print(book.get_name())

