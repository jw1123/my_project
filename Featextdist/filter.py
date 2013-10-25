from pymongo import Connection
from numpy import arange


def filt(feat,fil):
    a,b = [],[]
    for j in arange(0,len(feat)):
        try:
            a += feat[j]
        except:
            a = feat
    for h in arange(int(len(a)/fil)):
        try:
            k = sum(a[h*fil:(h+1)*fil])/fil
        except:
            k = sum(a[h*fil:len(a)])/len(a[h*fil:len(a)])
        b.append(k)
    return b

if __name__ == "__main__":
    con = Connection()
    db = con.extr_db
    song = db.song
    song1 = db.song1
    #db.song1.drop()

    s = db.song.find(timeout=False)

    for so in s:
        if so['id']>1:
            mf = filt(so['features'][0]['mfcc'][0]['default'],100)
            ch = filt(so['features'][0]['chromagram'][0]['default'],50)
            lin = filt(so['features'][0]['linearpower'][0]['default'],10)
            print so['metadata']
            song1.insert({
                'id':so['id'],
                'metadata':so['metadata'],
                'features':[{
                'mfcc':[{'default_filter':mf}],
                'chromagram':[{'default_filter':ch}],
                'linearpower':[{'default_filter':lin}],
                }],
                })




