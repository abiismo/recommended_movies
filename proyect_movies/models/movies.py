import requests 
import os
from dotenv import load_dotenv
from pathlib import Path
from .retry_gets import make_session

env_path = Path(__file__).parent / ".env" # Search my current file
load_dotenv(dotenv_path=env_path) # The values ​​from the .env file can be used  


def search_movie(query):
    TMBD_TOKEN = os.getenv('TMBD_TOKEN')
    
    if TMBD_TOKEN is None: # Connecting to the '.env' file, just failed
        return None

    session = make_session()

    try:
        headers = {
            "Authorization": f"Bearer {TMBD_TOKEN}",
            "accept": "application/json"
        }
    
        params = {
            "query": query
        }

        response = session.get(
            "https://api.themoviedb.org/3/search/movie", # Another form to re-write this
            headers=headers,
            params=params,
            timeout=(3.05 , 27)
        )

        return response.json() # Convert my answer variable into a Python dictionary
        
    except requests.exceptions.RequestException as error:
            print("An error ocurred", error)






