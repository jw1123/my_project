#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linalg, array, arange

class Dist:

    def __init__(self, song_collection, dist_collection):
        self.so = song_collection
        self.di = dist_collection

    def iter(self):
        l = arange(0,3)
        s = self.so.find(timeout=False).skip(1)
        r = self.so.find(timeout=False).skip(1)
        j = 2
        for song1 in s:
            print "_______________________"
            print song1['metadata']['titel']
            print "_______________________"
            for song2 in r:
                if song2['id'] > song1['id']:
                    distances = []
                    summe = 0
                    print song2['metadata']['titel']
                    feat_arr1, nam_arr1 = self.list_to_array(song1)
                    feat_arr2, nam_arr2 = self.list_to_array(song2)
                    for i in l:
                        distances.append(self.calc(feat_arr1[i],feat_arr2[i]))
                    try:
                        summe = sum(distances)/3
                    except:
                        summe = "unknown"
                    self.di.insert({
                    '_id': j,
                    'source': song1['id'],
                    'target': song2['id'],
                    nam_arr1[0]:{'default':distances[0]},
                    nam_arr1[1]:{'default':distances[1]},
                    nam_arr1[2]:{'default':distances[2]},
                    'total':{'default':summe}
                    })
                    print j, summe
                    j += 1
            r.rewind()


    def list_to_array(self,song):
        f = song['features']
        feat_array, name_array = [], []
        for fe in f:
            acc = f[str(fe)]
            m1 = acc['default']
            feat_array.append(self.conversion(m1))
            name_array.append(str(fe))
        return feat_array, name_array


    def conversion(self,list1):
        #try:
            #x = int(len(list1))
            #y = int(len(list1[0]))
            #return array(list1).reshape(x,y)
        #except:
        new_list = zip(*[iter(list1)]*2)
        x = int(len(new_list))
        y = 2
        return array(new_list).reshape(y,x)

    def calc(self,p,q):
        if p.shape[1] > q.shape[1]:
            d2 = self.reshap(p,q)
            return d2
        elif p.shape[1] < q.shape[1]:
            d2 = self.reshap(q,p)
            return d2
        elif p.shape == q.shape:
            d2 = linalg.norm(p-q)
            return d2
        else:
            return "unknown"
        

    def reshap(self,p,q):
            x = p.shape[1]/q.shape[1]
            pa = p.reshape(p.shape[1],p.shape[0])
            qa = q.reshape(q.shape[1],q.shape[0])
            qli = int(x)*qa.tolist()
            q1 = qli + qli[0:len(pa.tolist())-len(qli)]
            q1a = array(q1).reshape(p.shape[0], p.shape[1])
            return linalg.norm(p-q1a) #Calculates the distance

"""
    def ins(self,i,song1,song2,dist,nam):
        self.di.insert({
            '_id': i,
            'source': song1['id'],
            'target': song2['id'],
            nam[0]:[{'default':dist[0]}],
            nam[1]:[{'default':dist[1]}],
            nam[2]:[{'default':dist[2]}],
            nam[3]:[{'default':dist[3]}],
            nam[4]:[{'default':dist[4]}],
            'total':[{'default':sum(dist)}]
            })
"""


