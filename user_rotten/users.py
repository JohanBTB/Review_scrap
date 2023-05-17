# -*- coding: utf-8 -*-
# Rotten Tomatoes


import requests
from bs4 import BeautifulSoup
import json
import os
class User:
    
    
    def __init__(self, name, min_reviews = 5):
        self.name = name      
        self.min_reviews = min_reviews
        self.__json_directory = "user_rotten\\users_json"
        self.__current_directory = os.getcwd()
        self.users = []
        self.__filename = f"users_{self.name}.json"
        
    def get_users(self, append = True, check_all = True):
        """
        This function is responsible for retrieving the information through web scraping.
        It does not perform any any writing operation
        Append indicates if you want to append new users and dont delete the file that is already there
        Check_all indicates that if there is  an existant user in this page, it indicates this point has already seen, so the function is interrupted
        """
        
        file_path = os.path.join(self.__current_directory, f"movie_rotten\\movies_json\\movies_{self.name}.json")
        
        if append:
            try:
                with open(os.path.join(self.__current_directory, self.__json_directory, self.__filename)) as f:
                    self.users = json.load(f)
                    hrefs = set([ x['href'] for x in self.users])    
                    
            except FileNotFoundError:
                print("No file to append new data...")
                hrefs = set()
        
        
        try:
            with open(file_path, 'r') as f:
                dict_movies = json.load(f)
        except FileNotFoundError:
            return print("File no found, omitting user...")
        
        print('Getting users...')
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        session.headers.update(headers)
        
        
        for i, dict_movie in enumerate(dict_movies):
            url = dict_movie['href']
            url = dict_movie['href'] + "/reviews?type=user"
            print(f"Retrieving users from {dict_movie['name']}...")


            response = session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            audience_reviews = list(soup.find_all('div', class_="audience-review-row"))
            for audience_review in audience_reviews:
                try:
                    meta_user = audience_review.find('div', class_="audience-reviews__name-wrap").find('a')
                    user_url = meta_user.get('href')
                    name = meta_user.text.strip()
                    if not url:
                        print(f"\t ? User {name} no found...")
                        continue
                    
                    user_url = "https://www.rottentomatoes.com" + user_url
                    
                    response2 = session.get(user_url, headers=headers)
                    soup2 = BeautifulSoup(response2.content, 'html.parser')
                    reviews = list(soup2.find_all('li',class_="ratings__user-rating-review"))
                    
                    if user_url in hrefs:
                        if not check_all: 
                            print("\t • This user has already been checked, closing execution...")
                            break
                        print(f"\t • User {name} already added...")
                        continue
                    
                    if len(reviews)<self.min_reviews:
                        print(f"\t - User {name} does not have enough reviews (Only {len(reviews)})...")
                        continue
                    
                    user = {}
                    user['name'] = name
                    user['href'] = user_url
                    user['n_reviews'] = len(reviews)
                    hrefs.add(user_url)
                    self.users.append(user)
                    print(f"\t + User {name} added...")
                except AttributeError:
                    print("Something fail looking for user's href")
                    

    
    def write_json(self):
        """
        This functions creates a JSON file for each webpage, if it does not exists, and rewrites the file
        """        
        try:
            file_path = os.path.join(self.__current_directory, self.__json_directory)
            os.makedirs(os.path.join(file_path), exist_ok=True)
            if self.users:
                with open(os.path.join(file_path, self.__filename), 'w') as f:
                    json.dump(self.users,f,indent = 4)
                print("JSON file done")
            else:
                print("No data")
        except Exception as e:
            print(f"Error writing the JSON file: {e}")


    def get_json(self):
        """
        This functions return the JSON file of the webpage if it exists.
        """
        
        try:
            with open(os.path.join(self.__current_directory, self.__json_directory, self.__filename)) as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print("No data found")
            return None