# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:18:13 2013

@author: jw
"""

from bregman.suite import *
import os
import os.path
from pylab import *





def ex_3a(x, y, ttl=''):
    """
    Cross similarity matrix of two signals, using CHROMA features
    """
    p = default_feature_params()
    p['nhop'] = 2205
    p['feature'] = 'chroma'
    p['sample_rate'] = 1000
    F = Features(x,p)
    G = Features(y,p)
    D = distance.euc_normed(F.X.T,G.X.T)
    imagesc(D.T)
    title(ttl)
    xlabel('x vectors')
    ylabel('y vectors')
    return D
    
    
if __name__ == "__main__":    
    audio_file_1 = os.path.split(bregman.__file__)[0]+os.sep+'audio'+os.sep+'cant_hold_us.wav'
    x, sr_x, fmt_x = wavread(audio_file_1)
    audio_file_2 = os.path.split(bregman.__file__)[0]+os.sep+'audio'+os.sep+'bohemian_rhapsody.wav'
    y, sr_y, fmt_y = wavread(audio_file_2)
    
    
ex_3a(x,x, 'Cross Similarity Matrix: CHROMA')