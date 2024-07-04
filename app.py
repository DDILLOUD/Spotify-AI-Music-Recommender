import streamlit as st
from recommender import sp, recommend_songs

st.title('Spotify Music Recommender')

search_query = st.text_input('Enter an artist name:')

if search_query:
    results = sp.search(q=search_query, type='artist')
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        st.write(f"Selected artist: {artist['name']}")
        
        # Get the artist's top tracks
        top_tracks = sp.artist_top_tracks(artist['id'])
        
        # Create a playlist from the top tracks
        playlist_tracks = [track['id'] for track in top_tracks['tracks']]
        
        if st.button('Get Recommendations'):
            with st.spinner('Generating recommendations...'):
                recommendations = recommend_songs(playlist_tracks)
            
            if recommendations:
                st.success('Here are your recommendations:')
                for i, track in enumerate(recommendations, 1):
                    st.write(f"{i}. {track['name']} by {track['artists'][0]['name']}")
            else:
                st.error('Unable to generate recommendations. Please try a different artist.')
    else:
        st.warning('No artist found with that name. Please try again.')

st.sidebar.header('How to use')
st.sidebar.write('''
1. Enter the name of an artist you like.
2. Click "Get Recommendations" to see song suggestions based on the artist's top tracks.
''')

st.sidebar.header('About')
st.sidebar.write('''
This app uses the Spotify API to analyze the audio features of an artist's top tracks and recommends similar songs.
''')
