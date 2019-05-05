import unittest

class LoveTestCase(unittest.TestCase):
    def test_love_score(self):
        lyrics = 'I love you'
        self.assertEqual(love(lyrics), 0)
        
    def test_love_score(self):
        lyrics = 'Love love love heart and sometimes it was not there. My affection for my lover or my wife died'
        self.assertEqual(love(lyrics), 0.2)
        
    def test_love_score(self):
        lyrics = "love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce"
        self.assertEqual(love(lyrics),0.4)
        
    def test_love_score(self):
        lyrics = "love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce relationships darling dear love heart loved cherish adore lover wife unconditional affection amore enchant muse"
        self.assertEqual(love(lyrics),0.6)
        
    def test_love_score(self):
        lyrics = "love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce relationships darling dear love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce relationships darling dear"
        self.assertEqual(love(lyrics),0.8)
        
    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(LoveTestCase)
# Run each test in suite
unittest.TextTestRunner().run(suite)  
