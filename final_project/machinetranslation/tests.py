import unittest
from translator import english_To_French, french_To_English

class TestEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertEqual(english_To_French('Two'), 'Deux')  
        self.assertEqual(english_To_French(''), '')  
        self.assertEqual(english_To_French('Hello'), 'Bonjour') 

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_To_English('Deux'), 'Two')  
        self.assertEqual(french_To_English(''), '') 
        self.assertEqual(french_To_English('Bonjour'), 'Hello') 

unittest.main()