import sys
from aubio import tempo, source
from numpy import arange, mean, median
import os
#FROM DEMO_TEMPO_PLOT.PY OF AUBIO DEMOS FOLDER


def tempo_ext(filename):
    win_s = 512                 # fft size
    hop_s = win_s / 2           # hop size

    samplerate = 11000

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate
    o = tempo("default", win_s, hop_s, samplerate)

    # tempo detection delay, in samples
    # default to 4 blocks delay to catch up with
    delay = 4. * hop_s

    # list of beats, in samples
    beats = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = int(total_frames - delay + is_beat[0] * hop_s)
            #print "%f" % (this_beat / float(samplerate))
            beats.append(this_beat)
        total_frames += read
        if read < hop_s: break

    #convert samples to seconds
    beats = map( lambda x: x / float(samplerate), beats)

    bpms = [60./(b - a) for a,b in zip(beats[:-1],beats[1:])]
    print "BPM: ", median(bpms)*4


if __name__ == "__main__":
    for root,dirs,files in os.walk("/Users/jw/Desktop/Wave/"): #replace the path
            for file1 in files:
                if file1[len(file1)-3:len(file1)] == "wav":
                    tempo_ext("/Users/jw/Desktop/Wave/"+file1)

    



