import pickle
import pandas as pd # type: ignore
import streamlit as st # type: ignore


df = pickle.load(open('movie_dict.pkl', mode='rb'))
df = pd.DataFrame(df)
# print(df)

similarity = pickle.load(open('similarity.pkl', mode='rb'))
# print(similarity)


def recommend(movie):
    
    recommended_movies = []

    movie_index = df[df['title'] == movie].index[0]  
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in movie_list:
#         print(i[0])
        recommended_movies.append(df.iloc[i[0]].title)

    return recommended_movies


# Streamlit Web-App

st.title(':red[Netflix Movie Recommendation System]')
selected_movie = st.selectbox('Choose your movie: ', df['title'].values)
btn = st.button('Recommend')


if btn:
    movies_list = recommend(selected_movie)

    for i in movies_list:
        st.write(i)























