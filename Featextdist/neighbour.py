from pymongo import Connection

con = Connection()
db = con.extraction

d = db.distance.find().limit(5000)
s = db.song.find()
#e = db.distance.find()

a = {}

minimum, maximum = [],[]

for dis in d:
	if dis['source'] == 3:
		a.update({dis['target']:dis['total'][0]['default_filter']})

for i in [0,1,2,3,4,5,6,7,8,9]:
	minimum.append(min(a, key=a.get))
	del a[min(a, key=a.get)]

for i in [0,1,2,3,4,5,6,7,8,9]:
	maximum.append(max(a, key=a.get))
	del a[max(a, key=a.get)]

d.rewind()
for dis in d:
	for m in minimum:
		if dis['target'] == m and dis['source'] == 3:
			print dis
print "___________________________________________"
d.rewind()
for dis in d:
	for m in maximum:
		if dis['target'] == m and dis['source'] == 3:
			print dis	


for song in s:
	if song['id'] == 3:
			print "source: ", song['metadata'][0]['song_name']
	for id_ in minimum:
		if song['id'] == id_:
			print "minimum: ", song['id'], song['metadata'][0]['song_name']

s.rewind()
for song in s:
	if song['id'] == 3:
			print "source: ", song['metadata'][0]['song_name']
	for id_ in maximum:
		if song['id'] == id_:
			print "maximum: ", song['id'], song['metadata'][0]['song_name']

	#if song['id'] == 3:
		#print song['metadata']
	#if song['id'] == minimum:
		#print song['metadata'], 


