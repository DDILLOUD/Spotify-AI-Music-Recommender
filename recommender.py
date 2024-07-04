import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from functools import lru_cache

# Replace with your own Client ID and Client Secret
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Set up the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@lru_cache(maxsize=100)
def get_track_features(track_id):
    features = sp.audio_features(track_id)[0]
    return {
        'danceability': features['danceability'],
        'energy': features['energy'],
        'key': features['key'],
        'loudness': features['loudness'],
        'mode': features['mode'],
        'speechiness': features['speechiness'],
        'acousticness': features['acousticness'],
        'instrumentalness': features['instrumentalness'],
        'liveness': features['liveness'],
        'valence': features['valence'],
        'tempo': features['tempo']
    }

def get_track_recommendations(track_ids, limit=10):
    recommendations = sp.recommendations(seed_tracks=track_ids[:5], limit=limit)
    return recommendations['tracks']

def create_feature_vector(track_ids):
    feature_vector = []
    for track_id in track_ids:
        features = get_track_features(track_id)
        feature_vector.append(list(features.values()))
    return feature_vector

def recommend_songs(track_ids, num_recommendations=10):
    if not track_ids:
        print("No tracks found.")
        return []
    
    playlist_features = create_feature_vector(track_ids)
    
    if not playlist_features:
        print("No valid features found for the tracks.")
        return []
    
    avg_features = pd.DataFrame(playlist_features).mean().values.reshape(1, -1)
    
    recommendations = get_track_recommendations(track_ids, limit=50)
    
    rec_features = create_feature_vector([track['id'] for track in recommendations])
    
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(rec_features)
    scaled_avg_features = scaler.transform(avg_features)
    
    similarities = cosine_similarity(scaled_avg_features, scaled_features)
    
    sorted_indices = similarities[0].argsort()[::-1]
    top_recommendations = [recommendations[i] for i in sorted_indices[:num_recommendations]]
    
    return top_recommendations
