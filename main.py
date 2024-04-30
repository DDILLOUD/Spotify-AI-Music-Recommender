import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with Spotify API
client_id = 'your_client_id'
client_secret = 'your_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_recommendations(artists):
    # Fetch recommendations based on user input
    recommendations = sp.recommendations(seed_artists=artists, limit=10)
    return recommendations['tracks']

def display_recommendations(recommendations):
    # Display recommendations
    for i, track in enumerate(recommendations):
        print(f"{i+1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

if __name__ == "__main__":
    # Example usage
    favorite_artists = ['6vWDO969PvNqNYHIOW5v0m', '3TVXtAsR1Inumwj472S9r4']  # Example artists
    recommendations = get_recommendations(favorite_artists)
    display_recommendations(recommendations)
