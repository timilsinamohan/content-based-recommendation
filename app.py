import streamlit as st
import pickle
import pandas as pd
import requests
import os
import zipfile
import gdown

# URLs to your files in Google Drive
MOVIES_DICT_URL = "https://drive.google.com/uc?export=download&id=1lGGJ6rqaKU1lCzTyR7joWL1YosvgeNna"
SIMILARITY_ZIP_URL = "https://drive.google.com/uc?export=download&id=1mgOO5_XmY5tamqjZw8OFzZOFhSoFd1W6"

# Download and load movies_dict.pkl
if not os.path.exists("movies_dict.pkl"):
    # st.write("Downloading movies_dict.pkl...")
    response = requests.get(MOVIES_DICT_URL, stream=True)
    with open("movies_dict.pkl", "wb") as f:
        for chunk in response.iter_content(32768):  # 32KB chunks
            if chunk:
                f.write(chunk)
    # st.write("Downloaded movies_dict.pkl")

# Download and extract similarity.pkl.zip
if not os.path.exists("similarity.pkl"):
    # st.write("Downloading similarity.pkl.zip...")
    gdown.download(id="1mgOO5_XmY5tamqjZw8OFzZOFhSoFd1W6", output="similarity.pkl.zip", quiet=False)
    # st.write("Downloaded similarity.pkl.zip")

    # Extract the .zip file
    # st.write("Extracting similarity.pkl.zip...")
    with zipfile.ZipFile("similarity.pkl.zip", "r") as zip_ref:
        zip_ref.extractall()  # Extract to the current directory
    # st.write("Extracted similarity.pkl.zip")

# Debugging: Check the size and content of the downloaded files
# st.write("Debugging downloaded files...")

# Check movies_dict.pkl
try:
    with open("movies_dict.pkl", "rb") as f:
        # st.write("movies_dict.pkl size:", os.path.getsize("movies_dict.pkl"))
        movies_dict = pickle.load(f)
        # st.write("movies_dict.pkl loaded successfully!")
except Exception as e:
    st.error(f"Error loading movies_dict.pkl: {e}")

# Check similarity.pkl
try:
    with open("similarity.pkl", "rb") as f:
        # st.write("similarity.pkl size:", os.path.getsize("similarity.pkl"))
        similarity = pickle.load(f)
        # st.write("similarity.pkl loaded successfully!")
except Exception as e:
    st.error(f"Error loading similarity.pkl: {e}")

# Convert movies_dict to a DataFrame
movies = pd.DataFrame(movies_dict)

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
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