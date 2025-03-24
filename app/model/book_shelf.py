from __future__ import annotations
from app.interface.aggredate import Aggredate
from app.model.book import Book
from app.interface.iterator import Iterator
from typing import List, Optional

class BookShelf(Aggredate):
    def __init__(self, max_size: int):
        self.books: List[Book] = []  # 空のリストで初期化
        self.max_size = max_size
    
    def get_book_at(self, index: int) -> Optional[Book]:
        return self.books[index]
    
    def append_book(self, book: Book):
        if len(self.books) < self.max_size:  # 最大サイズをチェック
            self.books.append(book)
        else:
            raise IndexError("BookShelf is full")
    
    def get_length(self) -> int:
        return len(self.books)
    
    def iterator(self) -> Iterator:
        # 循環参照のため遅延インポート
        from app.bookshelf_iterator import BookshelfIterator
        return BookshelfIterator(self)