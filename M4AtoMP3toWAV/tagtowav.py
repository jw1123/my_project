from mutagen.id3 import ID3
from ffmpegwrapper import FFmpeg, AudioCodec, Input, Output
import os
from subprocess import call


#t = open('test.txt','r')

i = 0

for root,dirs,files in os.walk("/Users/jonathan/Desktop/MP3tag/"): #replace the path
    for file1 in files:
        i += 1
        if file1[len(file1)-3:len(file1)] == "mp3":
            a = 0
            tag = ID3("/Users/jonathan/Desktop/MP3tag/"+file1)
            input1 = Input("/Users/jonathan/Desktop/MP3tag/"+file1)
            codec = AudioCodec("pcm_s16le")
            print "____________________________"
            print tag
            try:
                b = tag["TDRC"]
                a = 1
            except:
                a = 0

            if a == 1:
                call(["ffmpeg", "-i", "/Users/jonathan/Desktop/MP3tag/"+file1, "-ar", "11000", "/Users/jonathan/Desktop/Wave1/"+str(tag["TIT2"])+"-*-"+str(tag["TPE1"])+"-*-"+str(tag["TALB"])+"-*-"+str(tag["TCON"])+"-*-"+str(tag["TDRC"])+".wav"])
                #output = Output("/Users/jonathan/Desktop/Wave1/"+str(tag["TIT2"])+"-*-"+str(tag["TPE1"])+"-*-"+str(tag["TALB"])+"-*-"+str(tag["TCON"])+"-*-"+str(tag["TDRC"])+".wav", codec)
            else:
                call(["ffmpeg", "-i", "/Users/jonathan/Desktop/MP3tag/"+file1, "-ar", "11000", "/Users/jonathan/Desktop/Wave1/"+str(tag["TIT2"])+"-*-"+str(tag["TPE1"])+"-*-"+str(tag["TALB"])+"-*-"+str(tag["TCON"])+".wav"])
                #output = Output("/Users/jonathan/Desktop/Wave1/"+str(tag["TIT2"])+"-*-"+str(tag["TPE1"])+"-*-"+str(tag["TALB"])+"-*-"+str(tag["TCON"])+".wav", codec)
            #ffmpeg = FFmpeg("ffmpeg", input1, output)
            #ffmpeg.add_parameter('-ar','22000')
            #ffmpeg.run()




#t.close()

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