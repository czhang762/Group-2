import main
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
        
     

class LengthTestCase(unittest.TestCase):
    def test_zeroscore(self):
        self.assertEqual(length(11),0.0)

    def test_onescore(self):
        self.assertEqual(length(100),0.1)

    def test_twoscore(self):
        self.assertEqual(length(700),0.2)

    def test_threescore(self):
        self.assertEqual(length(1300),0.3)

    def test_fourscore(self):
        self.assertEqual(length(1700),0.4) 
    
    def test_fivescore(self):
        self.assertEqual(length(2100),0.5)

    def test_sixscore(self):
        self.assertEqual(length(2700),0.6)

    def test_sevenscore(self):
        self.assertEqual(length(3100),0.7)

    def test_eightscore(self):
        self.assertEqual(length(3700),0.8)
    
    def test_ninescore(self):
        self.assertEqual(length(4100),0.9)

    def test_fullscore(self):
        self.assertEqual(length(4700),1.0)

class MoodTestCase(unittest.TestCase):   

    def test_zeroscore(self):
        self.assertEqual(mood('You are the worst.'),0.0)

    def test_onescore(self):
        self.assertEqual(mood('i hate everything'),0.1)

    def test_twoscore(self):
        self.assertEqual(mood('I did not feel angry or depressed I did not feel anything at all I did not want to go to bed'),0.2)



    def test_fourscore(self):
        self.assertEqual(mood('bad things can happen quickly'),0.4) 
    
    def test_fivescore(self):
        self.assertEqual(mood('Within hours'),0.5)

    def test_sixscore(self):
        self.assertEqual(mood('On April 29 someone shared a post titled "Pete Buttigieg Sexually Assaulted Me" on Medium, a site that lets anyone upload stories, essays and any other bit of text. It was attributed to a college student named Hunter Kelly.'),0.6)

    def test_sevenscore(self):
        self.assertEqual(mood('i love everything. everything is super great.'),0.7)

    def test_eightscore(self):
        self.assertEqual(mood('I would do anything to make her happy. I could hear their happy laughter in the other room. She had a very happy childhood. They have had a very happy marriage.'),0.8)
    
    def test_ninescore(self):
        self.assertEqual(mood('happy unicorns are so hopeful'),0.9)


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
    
class ComplexityTestCase(unittest.TestCase):
    def test_zeroscore(self):
        self.assertEqual(complexity('I do not like bugs.'),0.0)

    def test_onescore(self):
        self.assertEqual(complexity('small small small small small small small small small small complexity'),0.1)

    def test_twoscore(self):
        self.assertEqual(complexity('small small small small small small small complexity'),0.2)

    def test_threescore(self):
        self.assertEqual(complexity('small small small small small equestrian'),0.3)

    def test_fourscore(self):
        self.assertEqual(complexity('small small small small small small small fabulous equestrian'),0.4) 
    
    def test_fivescore(self):
        self.assertEqual(complexity('small small small small small small small small fabulous equestrians gallavanting'),0.5)

    def test_sixscore(self):
        self.assertEqual(complexity('small small recursion small small recursion'),0.6)

    def test_sevenscore(self):
        self.assertEqual(complexity('fabulous equestrians gallavanting small small small small small'),0.7)

    def test_eightscore(self):
        self.assertEqual(complexity('fabulous equestrians gallavanting small small small small'),0.8)
    
    def test_ninescore(self):
        self.assertEqual(complexity('equestrians equestrians small small'),0.9)

    def test_fullscore(self):
        self.assertEqual(complexity('equestrians equestrians equestrians equestrians'),1.0)
       
class MainTest(unittest.TestCase):
    def test_MiniLyrics2(self):
        dir='Mini_Lyrics2'
        self.assertEqual(main(dir),'{'characterizations': [OrderedDict([('id:', '004'), ('artist:', 'Spice Girls'), ('title:', 'Sleigh Ride'), ('kid_safe:', 1), ('love:', 0), ('mood:', 0.7), ('length:',
 0.4), ('complexity:', 0)])]}')
            
if __name__== '__main__':
    unittest.main()
