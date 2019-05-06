# Group2 Project

Members:
Cindy Zhang cz2461
Christine Rothacker crr2153


# What is it?
Group2 Project is a tool that takes a directory to a folder filled with text files with the naming format 'id_number~song_artist~song_title.txt' and analyzes each file. 

# Packages Required to use Tool:


# Main Features:
The main features of the individual song files that this tool analyzes are:

kid safety score: Kid safety score is based upon the total number of curse words in the song with respect to the amount of cursewords in all of the other songs in the file. If it is very kid safe the score will be 1 and if it is not kid safe it will be 0.

love score: Love score is based upon the total number of love related words (i.e. love, heart etc) in the song. If there are a lot of occurences of love related words the score will be 1 and if there are 1 or less occurence of love words it will be 0.

mood score: Mood score analyzes the text of the song and returns a score from 0 to 1 based upon if the lyrics of the song are upbeat or dark. If the lyrics are extremely upbeat it returns 1. If the lyrics of the song are very dark then it returns 0. 

length score: Length score is based upon the song file size in bytes compared to the other files in the program. If the song file is smaller than 15 bytes it will return a 0 and if it is very large it will return a 1.

complexity score: Complexity score is based on the percent of words in the lyrics of a song that are longer than 7 letters. If the song is very complex ie has a large percentage of long words.
