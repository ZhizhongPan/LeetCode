import unittest
from Solution import two_sum

class TestStringMethods(unittest.TestCase):
    
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = [0, 1]
        self.assertEqual(two_sum(nums, target), result)

if __name__ == '__main__':
    unittest.main()