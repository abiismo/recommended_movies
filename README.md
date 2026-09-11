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
    "original_title": "Superman Returns"
    "overview": "Superman returns to discover his 5-year absence has allowed Lex Luthor to...",
    "popularity": 10.5205,
    "poster_path": "/385XwTQZDpRX2d3kxtnpiLrjBXw.jpg",
    "release_date": "2006-06-28",
    "title": "Superman Returns",
    "video": false,
    "vote_average": 5.823,
    "vote_count": 4692
},
```

### GET /search

The function performs a search using a query parameter and accesses the TMDB API search to find a movie.

**Response:**
```
{
'page': 1, 'results': 
    {
    'adult': False, 
    'backdrop_path': '/yRBc6WY3r1Fz5Cjd6DhSvzqunED.jpg', 
    'genre_ids': [878, 12, 28], 
    'id': 1061474, 
    'title': 'Superman', 
    'original_language': 'en', 
    'original_title': 'Superman', 
    'overview': 'Superman, a journalist in Metropolis, embarks on a journey to reconcile his Kryptonian heritage with his human upbringing as Clark Kent.', 'popularity': 38.2691, 'poster_path': '/ldyfo0BKmz5rWtJJKCvwaNS4cJT.jpg', 'release_date': '2025-07-09', 
    'video': False, 
    'vote_average': 7.327, 
    'vote_count': 5410
    },
}
```

### POST /register

it receive two parameters and insert them into the data base. Also, important to know that the password get a salt to the password for security. 


**Parameters**:

user_name: it get the name of the user
user_password: it get the password of the user

**Example**: http://127.0.0.1:5000/register?user_name=nova,user_password=4321

**Response**

**URL:** `http://127.0.0.1:5000/register`

**Body:**
```json
{
    "user_name": "nova",
    "user_password": "4321"
}
```

now check your dabatabase. a new user with their password must be inserted. 

### POST /login

It receives two parameters, accesses the database, and checks whether a user with those characteristics exists. It will return a boolean value of *True* if the condition is met; otherwise, it will return *False*.

**Parameters**:

user_name: it get the name of the user
user_password: it get the password of the user

**Example**: http://127.0.0.1:5000/login?user_name=novita,user_password=4321


**Response**
```
{
    "login": true
}

```







