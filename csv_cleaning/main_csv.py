# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
import os
from csv_cleaning.csv_utils import dropping
from csv_cleaning.csv_utils import to_minutes
import numpy as np

# ---------------------------- Cleaning Users -------------------------------

# user_csv =  os.path.join(os.getcwd(), "csv_processing","csv_files","users.csv")
# users = pd.read_csv(user_csv, index_col = ['users_id'])
# users = dropping(users, ['href','n_reviews'], dropna = True)
# new_user_csv = os.path.join(os.getcwd(), "csv_cleaning","csv_files","users.csv")
# users.to_csv(new_user_csv, index=True)


# ---------------------------- Cleaning Reviews -------------------------------

# review_csv =  os.path.join(os.getcwd(), "csv_processing","csv_files","reviews.csv")
# reviews = pd.read_csv(review_csv, index_col = ['reviews_id'])
# review = dropping(reviews,['href','date','comment'], dropna = True)
# new_review_csv =  os.path.join(os.getcwd(), "csv_cleaning","csv_files","reviews.csv")
# reviews.to_csv(new_review_csv , index = True)


# ---------------------------- Cleaning Movies -------------------------------

movie_csv =  os.path.join(os.getcwd(), "csv_processing","csv_files","movies.csv")
movies = pd.read_csv(movie_csv, index_col = ['movies_id'])

# Filling spaces with "nan" value as ""
movies.fillna('', inplace = True)

# Merging both columns of genres in only one
movies['Genres'] = movies['Genre'] + movies['Genre(s)']

# Removing some characters from the table
movies = movies.replace({"\[|\]|TBA|tbd|\'":''}, regex=True)

# Merging two columns of release date and transforming form string to datetime type value. Finally transforming to minutes
movies['Release Date'] = movies['Release Date'].replace('', np.nan)
movies['Release Date'] = movies['Release Date'].fillna(movies['Release Date (Streaming)'])

## Deleting empty Release Date's values 
movies.drop(movies[movies['Release Date']==''].index, inplace = True)

movies['Release Date'] = pd.to_datetime(movies['Release Date'])
movies['Runtime'] = movies['Runtime'].apply(to_minutes)

# Cleaning genres
movies['Genres'] = movies['Genres'].replace({", ":'|', "Mystery&thriller":'Mystery','Sci-Fi':'Sci-fi'}, regex=True)

# Getting Dummies
genres = movies['Genres'].str.get_dummies('|')
movies = pd.merge(movies, genres, on="movies_id")

# Removing some columns
columns_to_drop = ['Aspect Ratio', 'Box Office (Gross USA)', 'critic_score','Distributor', 'Genre', 'Genres','Genre(s)', 'Director', 'Movie Facts', 'Original Language', 'Producer', 'Production Co', 'Rating','Release Date (Streaming)', 'Release Date (Theaters)', 'Sound Mix', 'Starring', 'Summary', 'View the collection', 'Writer']
movies = dropping(movies, columns_to_drop, dropna =False)


new_movie_csv =  os.path.join(os.getcwd(), "csv_cleaning","csv_files","movies.csv")
movies.to_csv(new_movie_csv , index = True)
