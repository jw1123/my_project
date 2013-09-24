# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:49:01 2013

@author: jw
"""

#ffmpeg -i sample.mp3 sample.wav


"""
from ffmpegwrapper import FFmpeg, Input, Output, AudioCodec


codec = AudioCodec('wav')

input_file = Input('/Users/jw/Desktop/FEBr/cant_hold_us')
output_file = Output('/Users/jw/Desktop/FEBr/cant_hold_us', codec)

FFmpeg('ffmpeg', input_file, output_file)
"""

from ffmpegwrapper import FFmpeg, AudioCodec, Input, Output

input1 = Input("cant_hold_us.mp3")
codec = AudioCodec("pcm_s16le")
output = Output("cant_hold_us.wav", codec)
ffmpeg = FFmpeg("ffmpeg", input1, output)
"""
# If you need the output at converting
with ffmpeg as process:
    for line in process.readlines():
        print line
"""
# If you don't need the output at converting
ffmpeg.run()




