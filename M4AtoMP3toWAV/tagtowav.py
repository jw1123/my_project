from mutagen.id3 import ID3
from ffmpegwrapper import FFmpeg, AudioCodec, Input, Output


t = open('test.txt','r')


for line in t:
	#print typeline,
	l = line[0:len(line)-1]
	print l[len(l)-3:len(l)]
	if l[len(l)-3:len(l)] == "m4a":
		input1 = Input(l)
		codec = AudioCodec("libmp3lame")
		output = Output(l[0:len(l)-3]+"mp3", codec)
		ffmpeg = FFmpeg("ffmpeg", input1, output)
		ffmpeg.run()

	if l[len(l)-3:len(l)] == "mp3":
		tag = ID3(l)
		input1 = Input(l)
		codec = AudioCodec("pcm_s16le")
		output = Output("/Users/jw/Desktop/Test/Wave/"+str(tag["TIT2"])+"-*-"+str(tag["TPE1"])+"-*-"+str(tag["TALB"])+".wav", codec)
		ffmpeg = FFmpeg("ffmpeg", input1, output)
		ffmpeg.run()

t.close()

"""
# If you need the output at converting
with ffmpeg as process:
    for line in process.readlines():
        print line
"""
# If you don't need the output at converting
#ffmpeg.run()



"""
TALB=Aerosmith
TCON=Rock
TDRC=2010
TIT2=Dream On
TPE1=Aerosmith
TRCK=1
"""