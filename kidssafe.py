 def kids_safe():
     import os
     import csv

     directory = "/Users/ChristineRothacker/Desktop/Lyrics/271~E-40~Neva-Broke.txt"
     curse_path = "/Users/ChristineRothacker/Desktop/cursewords.txt"
     
     a=open(curse_path, "r")
     curse_words=a.read().lower().split()
     print(curse_words)
     f = open(directory, "r")
     contents=f.read().lower().split()
     #print(contents)
     curse_count=0
     
     for i in contents:
         if i in curse_words:
             curse_count +=1.0
             if i.__contains__('*'):
                 curse_count +=1.0
                 print(curse_count)
                 print(curse_count/len(contents))


