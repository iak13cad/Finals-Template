"""
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Final Practical
@ASSESSME.ANALYZE: YES
"""

"""
This exam consists of three parts (A, B, and C). You are provided with:

    Test cases in a separate file named books_test.py to validate your code.

Objectives: Your solution should fully satisfy the requirements specified in each part to pass all tests. Pay attention to the choice of data structures.
Part A: Book Class

Complete the Book class according to the following requirements:

    Encapsulation: Ensure that all attributes are private and accessed via getter methods.
    Attributes: A book should have a title (string), author (string), and year of publication (int) specified at construction.
    String Representation:
        Implement __str__ to return the book’s information in the format: "{title}, by {author} ({year})".
        Implement __repr__ to return: "Book('{title}', '{author}', {year})".
    Equality: Two books are considered equal if they have the same title and author.
    Hashing: Implement the __hash__ method to make book objects hashable, using a combination of the book's title and author.
    Sorting: Implement comparison methods to sort books first by year, then by title, and finally by author.
"""

class Book:
    pass  # Implement this class based on the above requirements


"""
Part B: Library

Create a Library class with the following specifications:

    Encapsulation: Use appropriate private attributes.
    Constructor: Initialize shelves for different genres (e.g., "Fiction", "Non-fiction", "Science", "History").
    Shelves: Use a suitable data structure for the shelves that allows books to be added and retrieved efficiently.
    Methods:
        add_book(book, genre): Adds a book to the specified genre shelf. Raise ValueError for invalid genres.
        remove_book(title, author): Removes a book based on title and author from the library. Raise ValueError if the book is not found.
        find_books_by_author(author): Returns a list of books by the specified author, sorted by year of publication.
"""

class Library:
    pass  # Implement this class based on the above requirements


"""
Part C: Book Review Manager

Design a BookReviewManager class for storing and managing book reviews:

    Encapsulation: All attributes should be private.
    Constructor: Initializes storage for book reviews.
    Storage: Choose an appropriate data structure for storing reviews that allows for efficient searching and updating.
    Methods:
        add_review(book, review): Associates a review (text) with a book. Raise ValueError if the book does not exist.
        get_reviews(book): Retrieves all reviews for a specific book.
        average_rating(book): Computes and returns the average rating for a book based on its reviews.
"""

class BookReviewManager:
    pass  # Implement this class based on the above requirements
