
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from csv_processing.csv_utils import transform_to_csv
from csv_processing.csv_utils import visualize_csv
import os

""" Creating csv files"""
# user_path = os.path.join(os.getcwd(), "json_processing","json_files","all_users.json")
# transform_to_csv(user_path, "users.csv")

movie_path = os.path.join(os.getcwd(), "json_processing","json_files","all_movies.json")
transform_to_csv(movie_path, "movies.csv")

# review_path = os.path.join(os.getcwd(), "json_processing","json_files","all_reviews.json")
# transform_to_csv(review_path, "reviews.csv")


""" Visualizing csv files"""
# user_csv =  os.path.join(os.getcwd(), "csv_processing","csv_files","users.csv")
# users = visualize_csv(user_csv)-{}

# movie_csv =  os.path.join(os.getcwd(), "csv_processing","csv_files","movies.csv")
# movies = visualize_csv(movie_csv, parse_dates=['Release Date'])

# review_csv =  os.path.join(os.getcwd(), "csv_processing","csv_files","reviews.csv")
# reviews = visualize_csv(review_csv)


""" Changing some rows csv files """

# movies['Release Date'].replace({'TBA':np.nan}, inplace=True)
# movies['Release Date'] = pd.to_datetime(movies['Release Date'])

# visualize_csv(df = movies)

