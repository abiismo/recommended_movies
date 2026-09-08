from pathlib import Path
from dotenv import load_dotenv
import  mysql.connector
import os
import sys
from models.similar_movies import similar_movies
from collections import Counter


try:     
    from db import connection # Import the function that does the connection
except ImportError:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if root not in sys.path:
        sys.path.insert(0, root)
    from db import connection


def get_recommendations(id_user):
    try:
        conn = connection.get_connection()

        if conn is None: return None

        cursor = conn.cursor()

        query = """
        SELECT tmdb_movie_id FROM ratings WHERE id_user = %s and score >= 4
        """

        cursor.execute(query, (id_user,)) # TIP: (id_user,) --> will return a tuple, the comma sign is important to avoid errors LMAO
        
        ans = cursor.fetchall()
 
        all_results = []
        for movie in ans:
            data = similar_movies(movie[0])
            all_results.append(data["results"])


        res = [values[:3] for values in all_results] 

        unique_list = []
        for sublist in res:
            for element in sublist:
                unique_list.append(element)
# 
        # counter_list = []
        # for i in unique_list:
            # counter_list.append(i["id"])
        # 
        # s = Counter(counter_list).most_common()

        unique_movies = {}
        for movie in unique_list:
            unique_movies[movie["id"]] = movie
        final_ans = list(unique_movies.values())

        return final_ans
    
    except mysql.connector.Error as error:
        print(f"Connection data-base error: {error}")

    finally:
        if conn != None and conn.is_connected():
            conn.close()



