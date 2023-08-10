import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Python Programming", "John Smith", 29.99)
        self.assertEqual(book.title, "Python Programming")
        self.assertEqual(book.author, "John Smith")
        self.assertEqual(book.price, 29.99)

if __name__ == '__main__':
    unittest.main()
