from models.movies import search_movie as search
from models.similar_movies import similar_movies as similiar
from models.queries import get_recommendations as recommended
from flask import Flask, jsonify, request

app = Flask(__name__) # The current file

@app.route("/recommendations", methods=['GET'])
def get_recommendations():
    id_user = request.args.get('id_user', type=int)
    result = recommended(id_user)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)



