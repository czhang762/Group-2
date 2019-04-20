import os

def length(file1):
     size = os.stat(file1).st_size
     short_song = 0
     medium_song = 0.5
     long_song = 1
     if size <= 688:
         return short_song
     elif (size > 688) and (size <= 1344):
         return medium_song
     else:
         return long_song


