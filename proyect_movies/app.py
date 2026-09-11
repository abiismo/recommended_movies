from models.movies import search_movie as search
from models.similar_movies import similar_movies as similiar
from models.queries import get_recommendations as recommended
from flask import Flask, jsonify, request
from models.user import register, login

app = Flask(__name__) # The current file

@app.route("/recommendations", methods=['GET'])
def get_recommendations():
    id_user = request.args.get('id_user', type=int)
    result = recommended(id_user)
    return jsonify(result)

@app.route("/register", methods=['POST'])
def user_register():
    data = request.get_json()

    if data is None:
        return jsonify({"Error": "no JSON received"}), 400

    user_name = str(data.get('user_name'))
    user_password = str(data.get('user_password'))

    res = register(user_name, user_password)
    return jsonify({'register': res})


@app.route("/login", methods=['POST'])
def user_login():
    data = request.get_json()

    if data is None:
       return jsonify({"Error": "no JSON received"}), 400

    user_name = str(data.get('user_name'))
    user_password = str(data.get('user_password'))

    res = login(user_name, user_password)
    return str({'login',res})
    


if __name__ == "__main__":
    app.run(debug=True)

