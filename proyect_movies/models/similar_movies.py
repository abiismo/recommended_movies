import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from .retry_gets import make_session

path_env = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=path_env)

def similar_movies(movie_id):
    TMBD_TOKEN = os.getenv('TMBD_TOKEN')

    if not TMBD_TOKEN: 
        return None

    session = make_session()

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMBD_TOKEN}"
    }

    response = session.get(url, headers=headers, timeout=(3.05, 27))

    if response.status_code == 200:
        return response.json()

    else:
        print(f"Error: {response.status_code}")

