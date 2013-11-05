import os
from bregman.suite import MelFrequencyCepstrum, Chromagram, LinearPower, os
import contextlib
import wave
from numpy import arange

class Extr:

    def __init__(self, song_collection):
        self.so = song_collection
        #self.fe = feat_collection

    def filt(self,feat,fil):
        f =feat.tolist()
        a,b = [],[]
        for j in arange(0,len(f)):
            try:
                a += f[j]
            except:
                a = f
        for h in arange(int(len(a)/fil)):
            try:
                if(h!=0):
                    k = sum(a[h*fil-fil/2:(h+1)*fil])/(fil+fil/2)
                else:
                    k = sum(a[h*fil:(h+1)*fil])/fil
            except:
                k = sum(a[h*fil-fil/2:len(a)])/len(a[h*fil-fil/2:len(a)])
            b.append(k)
        return b


    def extr(self,x):
        mfcc = MelFrequencyCepstrum(x)
        chrom = Chromagram(x)
        lin = LinearPower(x)
        m = self.filt(mfcc.MFCC,100)
        c = self.filt(chrom.CHROMA,50)
        l = self.filt(lin.POWER,10)
        return m,c,l


    def extract(self): 

        i = 1
        #j = 0

        for root,dirs,files in os.walk("/Users/jonathan/Desktop/Wave/"): #replace the path
            for file1 in files:
                i += 1
                if file1[len(file1)-3:len(file1)] == "wav":
                    with contextlib.closing(wave.open("/Users/jonathan/Desktop/Wave/"+file1,"r")) as f:
                        frame = f.getnframes()
                        rate = f.getframerate()
                    m,c,li = self.extr("/Users/jonathan/Desktop/Wave/"+file1)
                    meta = file1.split("-*-")
                    try:
                        yea = meta[4][0:len(meta[4])-4]
                        gen = meta[3]
                    except:
                        yea = None
                        gen = meta[3][0:len(meta[3])-4]
                    self.so.insert({
                        'id':i,
                        'metadata': {
                        'title':meta[0],
                        'artist':meta[1],
                        'album':meta[2],
                        'genre':gen,
                        'year':yea,
                        'length':frame/float(rate)
                        },
                        'features': {
                        'mfcc':{'default':m},
                        'chromagram':{'default':c},
                        'linearpower':{'default':li},
                        },
                        })
                    print "________________"
                    print "id:          ", i
                    print "song:        ", meta[0]
                    print "length:      ", frame/float(rate)
                    try:
                        print "mfcc:        ", m[0:3]
                        print "chrom:       ", c[0:3]
                        print "lin:         ", li[0:3]
                    except:
                        print "***"


                    #j = self.featins(m,c,h,li,lo,self.fe,i,j)


"""
    def featins(self,m,c,h,li,lo,feat,id1,it):
        it +=1
        feat.insert({
            "id":it,
            "source":id1,
            "feature":"mfcc",
            "values":[{"default":m.tolist()}],
            })
        it += 1
        feat.insert({
            "id":it,
            "source":id1,
            "feature":"chromagram",
            "values":[{"default":c.tolist()}],
            })
        it += 1
        feat.insert({
            "id":it,
            "source":id1,
            "feature":"highfrequencyspectrum",
            "values":[{"default":h.tolist()}],
            })
        it += 1
        feat.insert({
            "id":it,
            "source":id1,
            "feature":"linearpower",
            "values":[{"default":li.tolist()}],
            })
        it += 1
        feat.insert({
            "id":it,
            "source":id1,
            "feature":"logfrequencyspectrum",
            "values":[{"default":lo.tolist()}],
            })
        return it
"""

#if __name__ == "__main__":




"""
    s = db.song.find()
    for song in s:
       print song['metadata']
    f = db.features.find()
    for feat in f:
        print feat['id'], feat['source']
"""

