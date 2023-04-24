# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import json
import os

class Movier:
    
    
    def __init__(self, name):
        self.name = name
        self.movies = []
        
        self.__json_directory = "movie\\movies_json"
        self.__current_directory = os.getcwd()
        self.__filename = f"movies_{self.name}.json"
    
    def get_json_directory(self):
        return self.__json_directory
    
    def get_current_directory(self):
        return self.__current_directory
    
    def get_movies(self):
        """
        This function is responsible for retrieving the information through web scraping.
        It does not perform any any writing operation
        """
        
        file_path = os.path.join(self.__current_directory, f"review\\reviews_json\\reviews_{self.name}.json")
        
        try:
            with open(file_path, 'r') as f:
                dict_movies = json.load(f)
        except FileNotFoundError:
            return print("File no found, omitting movies...")
        
        print(f"Getting movies from {self.name}...")
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        session = requests.Session()
        session.headers.update(headers)
        
        for i, dict_movie in enumerate(dict_movies):
            url = dict_movie['href']
            movie_info = {}
            movie_info['name'] = dict_movie['movie']
            movie_info['href'] = url
            try:
                list_labels = ['Starring','Genre(s)']

                response = session.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                rows = list(soup.find_all('span', class_='label'))
                score = soup.find('span', class_='metascore_w')
                movie_info['score'] = score.text
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
        print('Movies retrieved, Done')
    
    
    
    def write_json(self):   
        """
        This functions creates a JSON file for each movie, if it does not exists, and rewrites the file
        """
        try:
            file_path = os.path.join(self.__current_directory, self.__json_directory)
            os.makedirs(file_path, exist_ok=True)
            if self.movies:
                with open(os.path.join(file_path, self.__filename), "w") as f:
                    json.dump(self.movies,f,indent=4)
                print("JSON file done")
            else:
                print("No data")
        except Exception as e:
            print(f"Error writing the JSON file: {e}")
            

    def get_json(self):
        """
        This functions return the JSON file of the movie if it exists.
        """
        
        try:
            with open(os.path.join(self.__current_directory, self.__json_directory, self.__filename)) as f:
                data = json.load(f)
                print("Retrieving data")
                return data
        except FileNotFoundError:
            print("No data found")