import unittest

from translator import french_to_english, english_to_french

class e2f(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
if __name__ =='__main__':
    unittest.main()

