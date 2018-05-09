import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.palindrome = Palindrome()

    def test_isPalindrome(self):
        result = self.palindrome.isPalindrome('racecar')
        self.assertTrue('Palindrome',result)

if __name__ == '__main__':
    unittest.main()
