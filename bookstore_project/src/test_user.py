import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("user123", "user@example.com")
        self.assertEqual(user.username, "user123")
        self.assertEqual(user.email, "user@example.com")

if __name__ == '__main__':
    unittest.main()
