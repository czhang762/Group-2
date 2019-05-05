import argparse
import os
import re
from textblob import TextBlob


parser = argparse.ArgumentParser(description='song folder filepath')
parser.add_argument('indir', type=str, help='Input dir for songs folder')

args = parser.parse_args()

def get_name_info(title_str):
	
	# List that will be returned with the song information
	info_list=[] 
	id_pattern = r'^\d{3}\d*'
	
	#removing the unnecassary additional information in the brackets ie "[Album Version]"
	title_str=re.sub(r'\[[^()]*\]', '', title_str) 
	id_number=re.findall(id_pattern,title_str) 
	
	#adding songID number to the return list
	info_list.append(id_number[0]) 
	artist_pattern = r'(?<=~)(.*)(?=~)'
	artist= re.findall(artist_pattern, title_str)

	#adding artist to the return list
	info_list.append(artist[0].replace('-',' '))
	title_pattern = r'^(?:[^~]*\~){2}([^~]*)(?=\.)' ##pattern takes everything after the second ~ and before the . 
	title= re.findall(title_pattern, title_str)
	info_list.append(title[0].replace('-',' ').strip())
	
	# Returns list ['song id','song artist','song name']
	return info_list 

def love(lyrics):
    love_count=0
    love_words=["love","heart","loved","cherish","adore","lover","wife","unconditional","affection", "amore", "enchant", "muse", "relationship", "seduce", "relationships", "darling", "dear"]    
    for word in lyrics:
        if word in love_words:
            love_count += 1
        else:
            continue
            
    if love_count <= 1:
        return 0
    elif (love_count  <= 10) and (love_count  >1):
        return 0.2
    elif (love_count  <= 20) and (love_count  >10):
        return 0.4
    elif (love_count  <= 30) and (love_count  >20):
        return 0.6
    elif (love_count  <= 40) and (love_count  >30):
        return 0.8
    else:
        return 1	


def mood(lyrics):
    blob = TextBlob(lyrics)
    polar = blob.sentiment.polarity
    mood = round(polar,1)
    if mood <= -0.9:
        return 0
    elif (mood <= -0.7) and (mood > -0.9):
        return 0.1
    elif (mood <= -0.5) and (mood > -0.7):  
        return 0.2
    elif (mood <= -0.3) and (mood > -0.5):
        return 0.3
    elif (mood <= -0.1) and (mood > -0.3):
        return 0.4
    elif (mood <= 0.1) and (mood > -0.1):
        return 0.5
    elif (mood <= 0.3) and (mood > 0.1): 
        return 0.6
    elif (mood <= 0.5) and (mood > 0.3):  
        return 0.7
    elif (mood <= 0.7) and (mood > 0.5): 
        return 0.8
    elif (mood <= 0.9) and (mood > 0.7):   
        return 0.9
    else:
        return 1

def kids_safe(lyrics):
    curse_words=['anal', 'anus', 'arse', 'ass', 'ballsack', 'balls', 'bastard', 'bitch', 'biatch', 'blowjob', 'blow', 'job', 'bollock', 'bollok', 'boner', 'boob', 'bum', 'butt', 'clitoris', 'cock',  'crap', 'cunt', 'damn', 'dick', 'dildo', 'fag', 'fuck', 'goddamn', 'god', 'damn', 'hell', 'homo', 'jerk', 'jizz', 'knob', 'end', 'labia', 'muff', 'nigger', 'nigga', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy', 'queer', 'shitty', 'sex', 'shit', 'shits', 'slut', 'tit', 'tosser', 'twat', 'vagina', 'wank', 'whore', 'wtf']
    curse_count=0  
    song_lyrics=lyrics.replace('-', ' ').split()  
    for word in song_lyrics:
        if (word in curse_words) or (word.__contains__('*')):
            curse_count +=1
        else:
            continue
    if curse_count = 0:
        return 1
    elif (curse_count <= 3) and (curse_count >= 1):
        return 0.9
    elif (curse_count <= 5) and (curse_count > 3):
        return 0.8
    elif (curse_count <= 7) and (curse_count > 5):
        return 0.7
    elif (curse_count <= 9) and (curse_count > 7):
        return 0.6
    elif (curse_count <= 11) and (curse_count > 9):
        return 0.5
    elif (curse_count <= 13) and (curse_count > 11):
        return 0.4
    elif (curse_count <= 15) and (curse_count > 13):
        return 0.3
    elif (curse_count <= 17) and (curse_count > 15):
        return 0.2
    elif (curse_count <= 19) and (curse_count > 17):
        return 0.1
    else:
        return 0
            
class Song: 

	##creates a song object with the calculated characterizations as the attributes
	def __init__(self, lyrics, size):
		self.kid_safe_score=kid_safe(lyrics)
		self.love_score=love(lyrics)
		self.mood_score=mood(lyrics)
		self.length_score=length(size)
		self.complexity_score=complexity(lyrics)

	##creates and returns a dictionary with all of the characterizations
	def to_dict(self, song_info):
		song_dict={"id":song_info[0],"artist":song_info[1],"title":song_info[2],"kid_safe":self.kid_safe_score,"love":self.love_score,"mood":self.mood_score,"length":self.length_score,"complexity":self.complexity_score}
		return song_dict

Final_Song_Dictionary={}
List_of_Song_Dictionaries=[]
for filename in os.listdir(args.indir):
	if filename.endswith(".txt"):
		song_info_from_title=get_name_info(filename) 
		song_path=args.indir+"/"+filename
		song_size=os.stat(song_path).st_size
		with open(song_path) as song_file:
			song_lyrics=song_file.read().lower()
			curr_song=Song(song_lyrics, song_size)
			current_song_dict=curr_song.to_dict(song_info_from_title)
			List_of_Song_Dictionaries.append(current_song_dict)

Final_Song_Dictionary{"characterizations":List_of_Song_Dictionaries}
print(Final_Song_Dictionary)
