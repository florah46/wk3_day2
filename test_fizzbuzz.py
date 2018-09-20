import unittest
from fizzbuzz import fizzbuzz

class fizzbuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertTrue(fizzbuzz(['3, 12,2,7,0,5,2,9,0,4,7,9,2,3'],[]), 'fizzbuzz')

    def test_fizzbuzz(self):
         self.assertTrue(fizzbuzz(['3,9,4,w,3,5,e,7,1,2'], ['2,4']), 'fizz')

    def test_fizzbuzz(self):
         self.assertTrue(fizzbuzz(['3,7,d,3,6,d,g'], ['2,4,6']), 'buzz')

    def test_fizzbuzz(self):
         self.assertTrue(fizzbuzz(['3,10,2'], ['w,5,7,9,1,3,5,7,8,9']), 'Error')
    
if __name__ == "__main__":
    unittest.main()      