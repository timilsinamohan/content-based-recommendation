# Content-Based Movie Recommender System

This repository contains a content-based movie recommender system that leverages movie metadata from TMDB. The system is built with a focus on simplicity and ease-of-use, featuring a Streamlit front end and a model developed using a Jupyter Notebook.

## Data Source

The data used in this project can be found on Kaggle:

- **[TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)**  
  The dataset is freely available for public use.

## Model Development

The main recommendation model is developed in the notebook:

- `movies_recommender_system.ipynb`

This notebook outlines the process of data preparation, feature engineering, and model development.

## Front End

The user interface is built using the [Streamlit](https://streamlit.io/) framework, providing an interactive way to explore movie recommendations.

## Live Demo

A live demo of the application is available at:

- **[Content-Based Recommendation Demo](https://content-based-recommendation.onrender.com/)**

> **Note:** The demo might load slowly on Render due to resource constraints.

## Getting Started

To run the application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/timilsinamohan/content-based-recommendation.git
   cd content-based-recommendation
2. **Install dependencies:**
    ```bash
   pip install -r requirements.txt
4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

