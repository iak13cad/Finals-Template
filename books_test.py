import pytest
from library_management_system import Book, Library, BookReviewManager

# Tests for the Book class
def test_book_creation():
    book = Book("1984", "George Orwell", 1949)
    assert book.get_title() == "1984"
    assert book.get_author() == "George Orwell"
    assert book.get_year() == 1949


def test_book_str():
    book = Book("1984", "George Orwell", 1949)
    assert str(book) == "1984, by George Orwell (1949)"


def test_book_repr():
    book = Book("1984", "George Orwell", 1949)
    assert repr(book) == "Book('1984', 'George Orwell', 1949)"


def test_book_equality():
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("1984", "George Orwell", 1949)
    book3 = Book("Animal Farm", "George Orwell", 1945)
    assert book1 == book2
    assert book1 != book3


def test_book_hash():
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("1984", "George Orwell", 1949)
    assert hash(book1) == hash(book2)


def test_book_sorting():
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Animal Farm", "George Orwell", 1945)
    book3 = Book("Brave New World", "Aldous Huxley", 1932)
    books = [book1, book2, book3]
    books.sort()
    assert books == [book3, book2, book1]


# Tests for the Library class
def test_library_add_and_remove_book():
    lib = Library()
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Animal Farm", "George Orwell", 1945)
    lib.add_book(book1, "Fiction")
    lib.add_book(book2, "Fiction")
    assert lib.find_books_by_author("George Orwell") == [book2, book1]
    lib.remove_book("1984", "George Orwell")
    with pytest.raises(ValueError):
        lib.remove_book("1984", "George Orwell")


def test_invalid_genre():
    lib = Library()
    book = Book("1984", "George Orwell", 1949)
    with pytest.raises(ValueError):
        lib.add_book(book, "Unknown")


# Tests for the BookReviewManager class
def test_add_and_get_reviews():
    manager = BookReviewManager()
    book = Book("1984", "George Orwell", 1949)
    manager.add_review(book, "Excellent dystopian novel")
    assert manager.get_reviews(book) == ["Excellent dystopian novel"]


def test_average_rating():
    class Review:
        def __init__(self, rating):
            self.rating = rating

    manager = BookReviewManager()
    book = Book("1984", "George Orwell", 1949)
    manager.add_review(book, Review(4))
    manager.add_review(book, Review(5))
    assert manager.average_rating(book) == 4.5
