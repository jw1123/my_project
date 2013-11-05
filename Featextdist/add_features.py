# coding=utf-8
from pymongo import Connection
from numpy import arange
from math import sqrt

con = Connection()
db = con.extraction
s = db.song.find()
song_av = db.song_av
distance_av = db.distance_av

d = db.distance_av.find()

for di in d:
    print di




for son in s:
    for so in son:
        if so == 'metadata':
            #if son[so][0]['artist'] == u'Tie\u0308sto': #unicode('Tiësto'):
            print "______________________________"
            print son[so][0]['song_name']
            d,e,f = 0,0,0
            d = sum(son['features'][0]['mfcc'][0]['default'])
            e = sum(son['features'][0]['linearpower'][0]['default'])
            f = sum(son['features'][0]['chromagram'][0]['default'])
            song_av.insert({
                        'id':son['id'],
                        'metadata': {
                        'song_name':son[so][0]['song_name'],
                        'artist':son[so][0]['artist'],
                        'album':son[so][0]['album'],
                        'genre':son[so][0]['genre'],
                        'year':son[so][0]['year'],
                        'length':son[so][0]['length']
                        },
                        'features': {
                        'mfcc':{'default':d/len(son['features'][0]['mfcc'][0]['default'])},
                        'chromagram':{'default':f/len(son['features'][0]['chromagram'][0]['default'])},
                        'linearpower':{'default':e/len(son['features'][0]['linearpower'][0]['default'])},
                        },
                        })


s1 = db.song_av.find()
s2 = db.song_av.find()

for ss in s1:
    for sss in s2:
        if sss['id']>ss['id']:
            distance_av.insert({
                    'source': ss['id'],
                    'target': sss['id'],
                    'mfcc':{'default':sqrt(abs(ss['features']['mfcc']['default']**2-sss['features']['mfcc']['default']**2))},
                    'chromagram':{'default':sqrt(abs(ss['features']['chromagram']['default']**2-sss['features']['chromagram']['default']**2))},
                    'linearpower':{'default':sqrt(abs(ss['features']['linearpower']['default']**2-sss['features']['linearpower']['default']**2))},
                    'total':{'default':(sqrt(abs(ss['features']['mfcc']['default']**2-sss['features']['mfcc']['default']**2))+sqrt(abs(ss['features']['chromagram']['default']**2-sss['features']['chromagram']['default']**2)+sqrt(abs(ss['features']['linearpower']['default']**2-sss['features']['linearpower']['default']**2))))/3}
                    })
    s2.rewind()

d1 = db.distance_av.find()


