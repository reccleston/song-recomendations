import os
from dotenv import load_dotenv 
import spotipy
import joblib
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

load_dotenv('.env')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

def get_features(song):
    return spotify.audio_features(spotify.search(q=song, limit=1)['tracks']['items'][0]['uri'])[0]

# def getInfo(song, SongList):
#     print('this function runs: ', '\n', song)
#     for m in SongList:
#         print(m[0])
#     for row in SongList:
#         print('we made it')
#         print(row)
#         if row[0] == song:
#             print('MATCHED @%@%@%@%@%@%@')
#             return row[2:]
#     # fromt he billboard 

def makeTestPoint(features):
    
    data = pd.DataFrame(features, [0])
    data = data.assign(column_new_1=0.0, column_new_2=0.0, column_new_3=0.0, column_new_4=0.0)
    
    data = data[['column_new_1', 'column_new_2', 'column_new_3',
       'column_new_4', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms',
       'time_signature']]

    data = data.select_dtypes(['int', 'float']).values
    print(data)
    scaler = joblib.load('models/scaler.gz')    
    X = scaler.transform(data)

    print('\n', X, '\n')
    # fill in the blank not on billboard hits 
    return 0

