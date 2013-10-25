from extraction import Extr
from distance import Dist
from pymongo import Connection

if __name__ == "__main__":
    con = Connection()
    db = con.extraction
    song = db.song
    distance = db.distance
    #db.distance.drop()
    #db.song.drop()
    #features = db.features
    #db.features.drop()

    song.insert({
        'id':1,
        'param_key':'The audio sample rate_Number of Bands Per Octave for front-end filterbank___Number of cepstral \
        coefficients to use for cepstral features___Starting cepstral coefficient___Lowest band edge frequency of filterbank___\
        Highest band edge frequency of filterbank___FFT length for filterbank___FFT signal window length___FFT hop size___\
        FFT window size___Whether to use log output___Whether to use magnitude (False=power)___File extension for power files___\
        Whether to use critical band masking in chroma extraction___Whether to use onset-synchronus features___How much to tell \
        the user about extraction'
        })
    x = Extr(song)
    x.extract()

    y = Dist(song,distance)
    y.iter()


    #d = db.distance.find()
    #for dist in d:
    #    print dist


"""
    song.insert({
        'id':1,
        'param_key':'The audio sample rate_Number of Bands Per Octave for front-end filterbank___Number of cepstral \
        coefficients to use for cepstral features___Starting cepstral coefficient___Lowest band edge frequency of filterbank___\
        Highest band edge frequency of filterbank___FFT length for filterbank___FFT signal window length___FFT hop size___\
        FFT window size___Whether to use log output___Whether to use magnitude (False=power)___File extension for power files___\
        Whether to use critical band masking in chroma extraction___Whether to use onset-synchronus features___How much to tell \
        the user about extraction'
        })
    x = Extr(song)
    x.extract()

    s = db.song.find()
    for song in s:
       	print song['metadata']
    f = db.features.find()
    for feat in f:
        print feat['id'], feat['source']


   'sample_rate': 44100, # The audio sample rate
    'feature':'cqft',     # Which feature to extract (automatic for Features derived classes)
    'nbpo': 12,           # Number of Bands Per Octave for front-end filterbank
    'ncoef' : 10,         # Number of cepstral coefficients to use for cepstral features
    'lcoef' : 1,          # Starting cepstral coefficient
    'lo': 62.5,           # Lowest band edge frequency of filterbank
    'hi': 16000,          # Highest band edge frequency of filterbank
    'nfft': 16384,        # FFT length for filterbank
    'wfft': 8192,         # FFT signal window length
    'nhop': 4410,         # FFT hop size
    'window' : 'hamm',    # FFT window type 
    'log10': False,       # Whether to use log output
    'magnitude': True,    # Whether to use magnitude (False=power)
    'power_ext': ".power",# File extension for power files
    'intensify' : False,  # Whether to use critical band masking in chroma extraction
    'onsets' : False,     # Whether to use onset-synchronus features
    'verbosity' : 1       # How much to tell the user about extraction

"""