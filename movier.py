# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import json
import os

class Movier:
    
    
    def __init__(self, name):
        self.name = name

        self.movies = []
        
        
    def get_movies(self):
        
        directory = os.getcwd() + "\\reviews_json"
        file_path = directory + f"\\{self.name}"
        
        with open(file_path, 'r') as f:
            dict_movies = json.load(f)
        
        print('Getting reviews...')
        for i in range(len(dict_movies)):
            dict_movie = dict_movies[i]
            url = dict_movie['href']
            movie_info = {}
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
                list_labels = ['Starring','Genre(s)']
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                rows = list(soup.find_all('span', class_='label'))
                    
                for row in rows:
                    parent_span = row.find_parent()
                    spans = parent_span.find_all('span')
                    label = spans[0].text[:-1]
                    value = spans[1].text.strip()
                    if label in list_labels:
                        value = [x.strip() for x in value.strip().split(', ')] 
                    movie_info[label] = value
                
                self.movies.append(movie_info)
                print(f'Movie {i} done...')
            except Exception:
                print(f"Movie {i} ommited...")
        print('Getting reviews:, Done')
    
    
    
    def write_json(self):
        json_directory = "\\movies_json"
        current_directory = os.getcwd()
        
        if not os.path.exists(current_directory + json_directory):
            os.makedirs(json_directory)
            
        if self.movies:
            with open(f'{current_directory + json_directory}\\movies_{self.name}.json', 'w') as file:
                json.dump(self.movies, file, indent=4) 
        else:
            print('No data')
        print("JSON file done")
