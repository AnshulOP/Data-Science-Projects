# Importing the Streamlit library
import streamlit as st

# Importing the required libraries
import pickle
import pandas as pd

# Loading the pickled model
animes = pickle.load(open('animes_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Defining a function to recommend anime based on user input
def recommend(anime):
    anime_index = animes[animes['Name'] == anime].index[0] # Get the index of the anime
    distance = similarity[anime_index] # Get the similarity score
    anime_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:20] # Get the top 20 recommended animes
    recommended_animes = []
    for i in anime_list:
        recommended_animes.append(animes.iloc[i[0]].Name) # Get the name of the recommended anime
    return recommended_animes

# Setting up the Streamlit app
st.title('Anime Recommendation System')

# Creating a dropdown menu for the user to select an anime
movie_name = st.selectbox(
    'Enter or Select the name of the anime for which you want recommendations',
    animes['Name'].values)

# Creating a button for the user to click to get recommendations
if st.button('Recommendation'):
    recommendations = recommend(movie_name)
    for all_movies in recommendations:
        st.write(all_movies) # Displaying the recommended animes
