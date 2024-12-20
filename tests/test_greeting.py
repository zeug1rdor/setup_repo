# tests/test_greeting.py
import unittest
from src.greeting import greet

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

if __name__ == '__main__':
    unittest.main()