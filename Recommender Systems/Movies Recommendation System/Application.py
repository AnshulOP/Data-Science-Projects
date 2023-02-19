import streamlit as st
import pickle
import pandas as pd

# Define a function called "recommend" that takes a movie title as an argument
def recommend(movie):
    movie_index = movies[movies['Series_Title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:7]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].Series_Title)
    return recommended_movies

# Loading Movie Recommendation System elements
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Recommendation System')

# Making an input box that shows available movies
movie_name = st.selectbox(
'Enter or Select the name of the movie for which you want recommendations',
movies['Series_Title'].values)

# Making button for recommending movies
if st.button('Recommendation'):
    recommendations = recommend(movie_name)
    for all_movies in recommendations:
        st.write(all_movies)

