import unittest
from user import User
from book import Book
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        user = User("user123", "user@example.com")
        book = Book("Python Programming", "John Smith", 29.99)
        order = Order(user, [book], "Credit Card")
        self.assertEqual(order.user, user)
        self.assertEqual(order.items, [book])
        self.assertEqual(order.payment_method, "Credit Card")

if __name__ == '__main__':
    unittest.main()
