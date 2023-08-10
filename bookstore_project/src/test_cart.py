import unittest
from book import Book
from cart import Cart

class TestCart(unittest.TestCase):
    def test_cart_singleton(self):
        cart1 = Cart()
        cart2 = Cart()
        self.assertIs(cart1, cart2)

    def test_add_item_and_total(self):
        cart = Cart()
        book = Book("Python Programming", "John Smith", 29.99)
        cart.add_item(book)
        self.assertEqual(cart.total(), 29.99)

if __name__ == '__main__':
    unittest.main()
