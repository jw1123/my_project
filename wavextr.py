# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:43:59 2013

@author: jw
"""

from bregman.suite import *
from pylab import *


a1 = os.path.join(audio_dir,"chu.wav")
a2 = os.path.join(audio_dir,"br.wav")
a3 = os.path.join(audio_dir,"ra.wav")

mfc1 = MelFrequencyCepstrum(a1, sample_rate=10000)
mfc2 = MelFrequencyCepstrum(a2, sample_rate=10000)
mfc3 = MelFrequencyCepstrum(a3, sample_rate=10000)

x = mfc1.MFCC
y = mfc2.MFCC
z = mfc3.MFCC




#c1 = x - y
#c2 = x - z
#c3 = y - z

#distance1 = linalg.norm(c1)
#distance2 = linalg.norm(c2)
#distance3 = linalg.norm(c3)

#print distance1, distance2, distance3


"""
linspec = LinearFrequencySpectrum(a1, nfft=1024, wfft=512, nhop=256)
linspec.feature_plot(dbscale=True)
title('Wide-band Linear Spectrum Cant Hold Us')

chro = Chromagram(a1) #nfft=16384, wfft=8192, nhop=2205
chro.feature_plot(dbscale=True, normalize=True)
title('Chromagram Cant Hold Us')

mfcc = MelFrequencyCepstrum(a1)
mfcc.feature_plot(dbscale=True)
title('MFCC Cant Hold Us')


linspec1 = LinearFrequencySpectrum(a2, nfft=1024, wfft=512, nhop=256)
linspec1.feature_plot(dbscale=True)
title('Wide-band Linear Spectrum Bohemian Rhapsody')

chro1 = Chromagram(a2) #nfft=16384, wfft=8192, nhop=2205
chro1.feature_plot(dbscale=True, normalize=True)
title('Chromagram Bohemian Rhapsody')


mfcc1 = MelFrequencyCepstrum(a2)
mfcc1.feature_plot(dbscale=True)
title('MFCC Bohemian Rhapsody')


linspec2 = LinearFrequencySpectrum(a3, nfft=1024, wfft=512, nhop=256)
linspec2.feature_plot(dbscale=True)
title('Wide-band Linear Spectrum Rachmaninoff')

chro2 = Chromagram(a3) #nfft=16384, wfft=8192, nhop=2205
chro2.feature_plot(dbscale=True, normalize=True)
title('Chromagram Rachmaninoff')


mfcc2 = MelFrequencyCepstrum(a3)
mfcc2.feature_plot(dbscale=True)
title('MFCC Rachmaninoff')



rms1 = RMS(a1)
rms1.feature_plot(dbscale=True)
title('RMS Cant Hold Us')

rms1 = RMS(a2)
rms1.feature_plot(dbscale=True)
title('RMS Bohemian Rhapsody')

rms1 = RMS(a3)
rms1.feature_plot(dbscale=True)
title('RMS Rachmaninoff')
"""

