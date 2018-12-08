import unittest
from Solution import dp

class TestStringMethods(unittest.TestCase):

    def test_dp(self):
        self.assertEqual(dp(3), 3)

if __name__ == '__main__':
    unittest.main()