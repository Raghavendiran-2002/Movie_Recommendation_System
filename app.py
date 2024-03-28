import pandas as pd
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, render_template, jsonify

import mysql.connector as mysql
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env.prod')

load_dotenv(dotenv_path=dotenv_path)

conn = mysql.connect(user=os.getenv('DBUSER'), password=os.getenv('DBPASS'), auth_plugin='mysql_native_password',
                     host=os.getenv('DBHOST'), database=os.getenv('DATABASE'))

cursor = conn.cursor()


def createSimilarity():
    createTB = "SELECT * FROM movie_recommendation;"
    data = pd.read_sql(createTB, conn)
    cv = CountVectorizer()
    countMatrix = cv.fit_transform(data['genres'])
    similarity = cosine_similarity(countMatrix)
    return (data, similarity)


def getAllMovies():
    createTB = "SELECT movie_title FROM movie_recommendation;"
    movies = pd.read_sql(createTB, conn)
    return list(movies['movie_title'].str.capitalize())


def Recommend(movie):
    movie = movie.lower()
    try:
        data.head()
        similarity.shape
    except:
        (data, similarity) = createSimilarity()
    print(data)
    if movie not in data['movie_title'].unique():
        return 'Sorry! The movie you requested is not present in our database.'
    else:
        movieIndex = data.loc[data['movie_title'] == movie].index[0]
        lst = list(enumerate(similarity[movieIndex]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        # excluding first item since it is the requested movie itself and taking the top20 movies
        lst = lst[1:20]
        movieList = []
        for i in range(len(lst)):
            a = lst[i][0]
            movieList.append(data['movie_title'][a])
        return movieList


app = Flask(__name__, static_folder='Frontend/build',
            static_url_path='/')
CORS(app)


@app.route('/api/movies', methods=['GET'])
@cross_origin()
def movies():
    movies = getAllMovies()
    result = {'arr': movies}
    return jsonify(result)


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/similarity/<name>')
@cross_origin()
def similarity(name):
    movie = name
    recommendations = Recommend(movie)
    if type(recommendations) == type('string'):
        resultArray = recommendations.split('---')
        apiResult = {'movies': resultArray}
        return jsonify(apiResult)
    else:
        movieString = '---'.join(recommendations)
        resultArray = movieString.split('---')
        apiResult = {'movies': resultArray}
        return jsonify(apiResult)


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
