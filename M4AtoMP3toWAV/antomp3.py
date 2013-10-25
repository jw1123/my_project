from mutagen.id3 import ID3
from ffmpegwrapper import FFmpeg, AudioCodec, Input, Output
import os



for root,dirs,files in os.walk("/Users/jonathan/Desktop/Music1"): #replace the path
    for file1 in files:
        if file1[len(file1)-3:len(file1)] == "m4a":
            input1 = Input(file1)
            codec = AudioCodec("libmp3lame")
            output = Output("/Users/jonathan/Desktop/Music1/MP3/"+file1[0:len(file1)-3]+"mp3", codec) #replace the path
            ffmpeg = FFmpeg("ffmpeg", input1, output)
            ffmpeg.run()




#t = open('test.txt','r')
"""
input1 = Input("01_Miami_2_Ibiza.m4a")
codec = AudioCodec("libmp3lame")
output = Output("01_Miami_2_Ibiza.mp3", codec)
ffmpeg = FFmpeg("ffmpeg", input1, output)
ffmpeg.run()
"""


"""
for line in t:
	#print typeline,
	l = line[0:len(line)-1]
	if l[len(l)-3:len(l)] != "mp3":
		input1 = Input(l)
		codec = AudioCodec("pcm_s16le")
		output = Output(l[0:len(l)-3]+"mp3", codec)
		ffmpeg = FFmpeg("ffmpeg", input1, output)
		ffmpeg.run()
"""