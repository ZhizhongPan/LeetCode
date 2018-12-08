import unittest
from Solution import divide_coquer_recu, dp_down_top

class TestStringMethods(unittest.TestCase):

    def test_divide_coquer_recu(self):
        triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
        self.assertEqual(divide_coquer_recu(0, 0, triangle),11)

    def test_dp_down_top(self):
        triangle = [[1], [3,4], [6,5,7], [4,1,8,3]]
        self.assertEqual(dp_down_top(triangle),10)

if __name__ == '__main__':
    unittest.main()