import os
import spotipy # type: ignore
print(spotipy.__version__)
from spotipy.oauth2 import SpotifyClientCredentials # type: ignore

spotify_client_id = os.environ.get('SPOTIFY_CLIENT_ID', '08375480bf754eb085634ceb141520a6')
spotify_client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET', 'YOUR_CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)