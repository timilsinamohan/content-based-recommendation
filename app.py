import streamlit as st
import pickle
import pandas as pd
import requests
import os

# URLs to your files in Google Drive
MOVIES_DICT_URL = "https://drive.google.com/uc?export=download&id=1lGGJ6rqaKU1lCzTyR7joWL1YosvgeNna"
SIMILARITY_URL = "https://drive.google.com/uc?export=download&id=1Jfy8zB_MwJg343HbtvD4tPutADg4Ak_F"

# Function to download files from Google Drive
def download_file_from_google_drive(file_id, destination):
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()

    # Initial request to get the confirmation token
    response = session.get(URL, params={"id": file_id}, stream=True)
    token = None
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            token = value
            break

    # Download the file with the confirmation token
    if token:
        params = {"id": file_id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    # Save the file
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

# Download and load movies_dict.pkl
if not os.path.exists("movies_dict.pkl"):
    st.write("Downloading movies_dict.pkl...")
    download_file_from_google_drive("1lGGJ6rqaKU1lCzTyR7joWL1YosvgeNna", "movies_dict.pkl")
    st.write("Downloaded movies_dict.pkl")

# Download and load similarity.pkl
if not os.path.exists("similarity.pkl"):
    st.write("Downloading similarity.pkl...")
    download_file_from_google_drive("1Jfy8zB_MwJg343HbtvD4tPutADg4Ak_F", "similarity.pkl")
    st.write("Downloaded similarity.pkl")

# Load the files
with open("movies_dict.pkl", "rb") as f:
    movies_dict = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Convert movies_dict to a DataFrame
movies = pd.DataFrame(movies_dict)

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Streamlit app
st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select Your Movie", movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
#
# def recommend(movie):
#     movie_index = movies[movies["title"] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch poster from PI
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies,recommended_movies_posters
#
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
#
# st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox('Select Your Movie', movies['title'].values)
#
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])
