from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

movies = joblib.load('movies.pkl')
similarity = joblib.load('similarity.pkl')


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:7]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


@app.route('/', methods=['GET', 'POST'])
def index():

    movie_list = sorted(movies['title'].values)

    selected_movie = None
    recommendations = []

    if request.method == 'POST':

        selected_movie = request.form['movie']
        print("Selected movie:", selected_movie)

        recommendations = recommend(selected_movie)
        print("Recommendations:", recommendations)

    return render_template(
        'index.html',
        movies=movie_list,
        selected_movie=selected_movie,
        recommendations=recommendations
    )


if __name__ == '__main__':
    app.run(debug=True)