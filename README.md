# Recommended movies 

## About

Recommended movies based on the rating of the user, pick up the id of the movie and does a search of similar movies through of an API

## Prerequisites

##### Before you continue, ensure you have met the following requirements:

* you have the latest version of python 
* you have the flask librarie already installed 
* have a knowledge about SQL statements
* after reading the TMDB API you can use and understand some functionalities of this project: 
    ```
    https://developer.themoviedb.org/docs/getting-started
    ```


## Installation

##### Follow these steps to install everything correctly.

* Clone the repository
* Install dependencies 
* Configure the .env
    ```
    DB_HOST=
    DB_USER=
    DB_PASSWORD=
    DB_NAME=
    ```
* Create a basic database with the schema (user, and ratings)
* run main.py and app.py


```bash
git clone https://github.com/abiismo/recommended_movies
```

## Usage

### GET /recommendations

It retrieves the user's movie from the database and fetches only those movies with a rating of 4 or higher.

**Example:** http://127.0.0.1:5000/recommendations?id_user=1 

**Response:**
```
{
    "adult": false,
    "backdrop_path": "/8eRscFbRYl681zDfkjv1jjW1KAA.jpg",
    "genre_ids": [878, 28, 12],
    "id": 1452,
    "original_language": "en",
    "original_title": "Superman Returns",
    "overview": "Superman returns to discover his 5-year absence has allowed Lex Luthor to...",
    "popularity": 10.5205,
    "poster_path": "/385XwTQZDpRX2d3kxtnpiLrjBXw.jpg",
    "release_date": "2006-06-28",
    "softcore": false,
    "title": "Superman Returns",
    "video": false,
    "vote_average": 5.823,
    "vote_count": 4692
},
```
 









