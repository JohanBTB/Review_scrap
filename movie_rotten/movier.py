# -*- coding: utf-8 -*-
# Rotten Tomatoes


import requests
from bs4 import BeautifulSoup
import json
import os

class Movier:
    


    def __init__(self, name, url="https://www.rottentomatoes.com/browse/movies_at_home/affiliates:paramount_plus"):
        self.name = name
        self.movies = []
        self.genres = """    ACTION
            ADVENTURE
            ANIMATION
            ANIME
            BIOGRAPHY
            COMEDY
            CRIME
            DOCUMENTARY
            DRAMA
            ENTERTAINMENT
            FAITH & SPIRITUALITY
            FANTASY
            GAME SHOW
            LGBTQ+
            HEALTH & WELLNESS
            HISTORY
            HOLIDAY
            HORROR
            HOUSE & GARDEN
            KIDS & FAMILY
            MUSIC
            MUSICAL
            MYSTERY & THRILLER
            NATURE
            NEWS
            REALITY
            ROMANCE
            SCI-FI
            SHORT
            SOAP
            SPECIAL INTEREST
            SPORTS
            STAND-UP
            TALK SHOW
            TRAVEL
            VARIETY
            WAR
            WESTERN""".split('\n')
        
        self.genres = list(map(lambda x: "~genres:"+x.strip().lower(), self.genres))
        # self.genres = ['~genres:action']
        self.audience =list(map(lambda x: "~audience:"+x, ['spilled','upright']))
        # self.audience = []
        self.url = url
        
        self.__json_directory = "movie_rotten\\movies_json"
        self.__current_directory = os.getcwd()
        self.__filename = f"movies_{self.name}.json"
    
    def get_json_directory(self):
        return self.__json_directory
    
    def get_current_directory(self):
        return self.__current_directory
    
    def update_movie_info(self, indexes, movie_keys, movie_values):
        for index in indexes:  
            try:
                genre_i = movie_keys.index(index)
                movie_values[genre_i] = movie_values[genre_i].replace('\n', '').replace(' ','').replace(',',', ')
            except ValueError as e:
                # print(f"error: {e}")
                pass
                    
    
    def get_movies(self):
        """
        This function is responsible for retrieving the information through web scraping.
        It does not perform any any writing operation
        """
        
        print('Getting movies...')
        visited_movie_links = set()
        visited_movie_links.add("")
        
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        session.headers.update(headers)
        
        for sub_url in self.genres + self.audience:
            i = 5
            url = self.url + f"{sub_url}?page={i}"
            print(f"Reading page of {sub_url.split(':')[1].upper()}...")

            response = session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            tiles = list(soup.find_all(class_="js-tile-link"))
            if not tiles:
                print("No movies found, omitting...")
                continue

            for tile in tiles:
                
                critic_score = tile.find('score-pairs').get('criticsscore')
                audience_score = tile.find('score-pairs').get('audiencescore')
                name = tile.find('span',{'data-qa':'discovery-media-list-item-title'}).text.strip()
                date = tile.find('span',{'data-qa':'discovery-media-list-item-start-date'}).text.strip().replace('Streaming ', '')
                try:
                    if tile.find('a',{'data-qa':'discovery-media-list-item-caption'}):
                        href = tile.find('a',{'data-qa':'discovery-media-list-item-caption'}).get('href')
                    elif tile.find('a',{'data-track':"scores"}):
                        href = tile.find('a',{'data-track':"scores"}).get('href')
                    else: 
                        href = tile.get('href')
                    
                    href ="https://www.rottentomatoes.com" + href
                    if href in visited_movie_links:
                        print(f"\t • Movie {name} have been already accepted.")
                        continue
                except AttributeError:
                    href=""
                    print(f"\t - Href no found in {name}")
                    continue
                
                response2 = session.get(href)
                soup2 = BeautifulSoup(response2.content, 'html.parser')
                media_body = soup2.find("div", class_="media-body")
                
                if not media_body:
                    print(f"\t • Omitting body of {name}")
                    continue
                movie_keys = ['name','href','score','critic_score','Release Date']
                movie_values = [name, href, audience_score, critic_score, date]
                movie_values += [v.text.strip() for v in media_body.find_all('span', class_='info-item-value', attrs={'data-qa': 'movie-info-item-value'})]
                movie_keys += [k.text.strip().replace(':','') for k in media_body.find_all('b', class_='info-item-label', attrs={'data-qa': 'movie-info-item-label'})]
                indexes = ['Genre', 'Director','Distributor','Writer','Producer', 'Production Co']
                self.update_movie_info(indexes, movie_keys, movie_values)     
                
                try:
                    theater_i = movie_keys.index('Release Date (Theaters)')
                    movie_values[theater_i] = movie_values[theater_i][:movie_values[theater_i].index('\n')].strip()
                except ValueError as e:
                    # print(f"error: {e}")
                    pass
                
                movie = {}
                visited_movie_links.add(href)

                
                movie = {key: value for key, value in zip(movie_keys, movie_values)}
                
                self.movies.append(movie)
                print(f"\t + Movie {name} accepted")
    

    def write_json(self):   
        """
        This functions creates a JSON file for each movie, if it does not exists, and rewrites the file
        """
        
        try:

            file_path = os.path.join(self.__current_directory, self.__json_directory)
            os.makedirs(file_path, exist_ok=True)
            if self.movies:
                with open(os.path.join(file_path, self.__filename), 'w') as f:
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
            with open(os.path.join(self.__current_directory, self.__json_directory, f"movies_{self.name}.json")) as f:
                data = json.load(f)
                print("Retrieving data")
                return data
        except FileNotFoundError:
            print("No data found")
            return None