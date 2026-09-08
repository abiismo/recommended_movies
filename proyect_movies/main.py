import bcrypt 
from models.movies import search_movie
from models.similar_movies import similar_movies
from models.queries import get_recommendations
from models.user import register, login

queryRegister = str(input("Name: "))
queryPassword = str(input("Password: "))


register(queryRegister, queryPassword)

user_name = input("Username: ") 
password = input("Password: ")
# 
print(login(user_name, password)) 
#                         
# query = input("Movie: ")
# print(search_movie(query))
# 
# query2 = input("id: ")
# print(similar_movies(query2)) 

# query3 = int(input("Id: "))
# print(get_recommendations(query3))


 
# Presionando mayuscula + a, me da un salto al último caracter del texto --> Tambien si estoy en doble modo, puedo saltarme de una a insert...
# Estando dentro del modo normal de vim, presionando control + v me permite seleccionar texto...
# Con el modo visual block, también puedo seleccionar y eliminar con la letra d


