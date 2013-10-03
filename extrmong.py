from bregman.suite import MelFrequencyCepstrum, Chromagram, os, audio_dir
import pymongo as pm
from numpy import linalg, array



#Creating paths to the wav file (aduio_dir is the default path to the audio folder in the bregman folder)
a1 = os.path.join(audio_dir,"chu.wav")
a2 = os.path.join(audio_dir,"br.wav")

#Calculates a MFC object for the wav file called by the respective path
mfc1 = MelFrequencyCepstrum(a1, sample_rate=10000)
mfc2 = MelFrequencyCepstrum(a2, sample_rate=10000)
#Calculates a Chromogram object for the wav file called by the respective path
chro1 = Chromagram(a1) #nfft=16384, wfft=8192, nhop=2205
chro2 = Chromagram(a2) #nfft=16384, wfft=8192, nhop=2205

#Access the MFCC array (numpy array)
x = mfc1.MFCC
y = mfc2.MFCC

#Access the CHROMA array (numpy array)
p = chro1.CHROMA
q = chro2.CHROMA




if __name__ == "__main__":

#_____________________________________SONG_COLLECTION_________________________________________#
	con = pm.Connection()
	db = con.test_db1 
	song = db.song #Creating or accessing a collection named song
	db.song.drop() #Clearing everything inside song

	#Inserting two songs into the song collection
	#The MFCC and CHROMA arrays have to be stored as 1D lists accomplished by x.tolist()
	song.insert({
		'_id':1,
		'song_name':'Can\'t Hold Us',
		'album':'The Heist',
		'features': [{'MFCC': x.tolist(), 'CHROMA':p.tolist()}], 
		'artist':'Macklemore & Ryan Lewis',
		'year':2012	
		})

	song.insert({
		'_id':2,
		'song_name':'Bohemian Rhapsody',
		'album':'A Night At The Opera',
		'features': [{'MFCC': y.tolist(), 'CHROMA':q.tolist()}],
		'artist':'Queen',
		'year': 1975		
		})


	#s = db.song.find()
	#for song in s:
	#	print song['song_name'] #Print all the song names inside the song collection





	#ft = s['features']
	#mf = ft[0]
	#print type(mf['MFCC'])
	
	#xf = pickle.loads(str(mf))

	

	#col = s.collection
	#print col


#________________________________________SONG_COMPARISON____________________________________________#
	distance = db.distance #Creating or accessing a collection named distance


	#Comparison of MFCC features
	if x.shape == y.shape:
		d1 = linalg.norm(x-y)
	elif x.shape[1] > y.shape[1]:
		#Reshaping the features in order to compare the dimensionality which are different
		#In fact, the first dimensionality (x.shape[0]) is the same for every feature,
		#if the same sample_rate has been applied
		xa = x.reshape(x.shape[1],x.shape[0])
		ya = y.reshape(y.shape[1],y.shape[0])
		#Filling the smaller feature (as a list) with itself, for the difference of length
		#between both lists
		y1 = ya.tolist() + ya.tolist()[0:len(xa.tolist())-len(ya.tolist())]
		y1a = array(y1).reshape(x.shape[0], x.shape[1]) #Reshaping again to create an array of the initial dimensions
		d1 = linalg.norm(x-y1a) #Calculates the distance
	elif x.shape[1] < y.shape[1]:
		xa = x.reshape(x.shape[1],x.shape[0])
		ya = y.reshape(y.shape[1],y.shape[0])
		x1 = xa.tolist() + xa.tolist()[0:len(ya.tolist())-len(xa.tolist())]
		x1a = array(x1).reshape(y.shape[0], y.shape[1])
		d1 = linalg.norm(y-x1a) #Calculates the distance


	#Comparison of CHROMA features
	if p.shape == q.shape:
		d2 = linalg.norm(p-q)
	elif p.shape[1] > q.shape[1]:
		pa = p.reshape(p.shape[1],p.shape[0])
		qa = q.reshape(q.shape[1],q.shape[0])
		q1 = qa.tolist() + qa.tolist()[0:len(pa.tolist())-len(qa.tolist())]
		q1a = array(q1).reshape(p.shape[0], p.shape[1])
		d2 = linalg.norm(p-q1a) #Calculates the distance
	elif p.shape[1] < q.shape[1]:
		pa = p.reshape(p.shape[1],p.shape[0])
		qa = q.reshape(q.shape[1],q.shape[0])
		p1 = pa.tolist() + pa.tolist()[0:len(qa.tolist())-len(pa.tolist())]
		p1a = array(p1).reshape(q.shape[0], q.shape[1])
		d2 = linalg.norm(q-p1a) #Calculates the distance


	distance.insert({
		'_id': 1,
		'id1': 1,
		'id2': 2,
		'MFCC': d1,
		'CHROMA': d2
		})



	# Removing everything from both collections and erasing the collections
	db.song.remove()
	db.song.drop()
	db.distance.remove()
	db.distance.drop()