import unittest
from Solution import dp, dp2

class TestStringMethods(unittest.TestCase):

    def test_dp(self):
        matrix = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(dp(matrix),7)

    def test_dp2(self):
        matrix = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(dp2(matrix),7)

if __name__ == '__main__':
    unittest.main()