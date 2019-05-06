import unittest


class GetNameInfoTestCase(unittest.TestCase):
    def test_songID(self):
        c=get_name_info('1234~Spice-Ladies~Rock-Road[lala].txt')
        self.assertEqual(c[0],'1234')
    def test_song_artist(self):
        name=get_name_info('1234~Spice-Ladies~Rock-Road[lala].txt')
        self.assertEqual(name[1],'Spice Ladies')
    def test_song_name(self):
        s_name=get_name_info('1234~Spice-Ladies~Rock-Road[lala].txt')
        self.assertEqual(s_name[2],'Rock Road')

class LoveTestCase(unittest.TestCase):
    def test_not_love_song(self):
        lyrics = 'I love you'
        self.assertEqual(love(lyrics), 0)  
    
    def test_love_score_2(self):
        lyrics = 'Love love love heart and sometimes it was not there. My affection for my lover or my wife died'
        self.assertEqual(love(lyrics), 0.2)
        
    def test_love_score_4(self):
        lyrics = "love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce"
        self.assertEqual(love(lyrics),0.4)
        
    def test_love_score_6(self):
        lyrics = "love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce relationships darling dear love heart loved cherish adore lover wife unconditional affection amore enchant muse"
        self.assertEqual(love(lyrics),0.6)
        
    def test_love_score_8(self):
        lyrics = "love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce relationships darling dear love heart loved cherish adore lover wife unconditional affection amore enchant muse relationship seduce relationships darling dear"
        self.assertEqual(love(lyrics),0.8)
        
    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(LoveTestCase)
# Run each test in suite
unittest.TextTestRunner().run(suite)  



class KidsSafeTestCase(unittest.TestCase):
    def test_no_curse(self):
        lyrics = "I hate everyone and I am proud of it."
        self.assertEqual(kids_safe(lyrics),1)
    
    def test_kids_score_9(self):
        lyrics = "I consider you to be a bastard and a bitch."
        self.assertEqual(kids_safe(lyrics),0.9)
    
    def test_kids_score_7(self):
        lyrics = "My favorite curse words are: anal anus arse ass ballsack balls."
        self.assertEqual(kids_safe(lyrics),0.7)
        
    def test_kids_score_5(self):
        lyrics = "I can be described as blowjob bollock boner bum clitoris cock dick dildo fuck nigger"
        self.assertEqual(kids_safe(lyrics),0.5)
        
    def test_kids_score_3(self):
        lyrics = "anal anus arse ass ballsack blowjob bollock boner bum clitoris cock dick dildo fuck"
        self.assertEqual(kids_safe(lyrics),0.3)
        
    def test_kids_score_1(self):
        lyrics = "anal anus arse ass ballsack blowjob bollock boner bum clitoris cock dick dildo fuck fuck fuck fuck fuck"
        self.assertEqual(kids_safe(lyrics),0.1)
        
    def test_not_kids_safe(self):
        lyrics = "biatch blowjob blow job bollock bollok boner boob bum butt clitoris cock crap cunt damn dick dildo fag fuck goddamn hell homo nigga penis piss prick pussy shit tit twat wank"
        self.assertEqual(kids_safe(lyrics),0)
    

            
suite = unittest.defaultTestLoader.loadTestsFromTestCase(KidsSafeTestCase)
# Run each test in suite
unittest.TextTestRunner().run(suite) 
