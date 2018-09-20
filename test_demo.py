import unittest
from demo import count_vowels

class TestDemo(unittest.TestCase):
    def test_count_vowels(self):
        self.assertTrue(count_vowels,('freedom'))
    
    
if __name__ == "__main__":
    unittest.main()