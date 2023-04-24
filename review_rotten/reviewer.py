# -*- coding: utf-8 -*-
# Rotten Tomatoes


import requests
from bs4 import BeautifulSoup
import json
import os

class Reviewer:

    
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.reviews = []
        self.__json_directory = "review_rotten\\reviews_json"
        self.__current_directory = os.getcwd()
        self.__filename = f"reviews_{self.name}.json"
    
    def get_json_directory(self):
        return self.__json_directory
    
    def get_current_directory(self):
        return self.__current_directory
    
    def get_reviews(self):
        """
        This function is responsible for retrieving the information through web scraping.
        It does not perform any any writing operation

        """
        file_path = os.path.join(self.__current_directory, f"user_rotten\\users_json\\users_{self.name}.json")
        if not os.path.exists(file_path):
            return print("File no found, omitting webpage")
        
        with open(file_path, 'r') as f:
            dict_users = json.load(f)
        
        print('Getting reviews...')
        
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        session.headers.update(headers)
        
        for i, dict_user in enumerate(dict_users):
            name = dict_user['name']
            url = dict_user['href']
            print(f"Reading reviews of {name}...")

            response = session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            try:
                reviews = list(soup.find_all('section',class_="bottom_divider ratings__user-rating"))
                for j, review in enumerate(reviews):
                    print(f'\tReading review {j+1}...')
                    try:
                        movie = review.find("a", class_="ratings__movie-title").text.strip()
                        stars = len(list(review.find('div', class_="ratings__rating-stars").find_all('span',class_="star-display__filled")))
                        date = review.find("a", class_="ratings__age").text.strip()
                        comment = review.find('p', class_="ratings__comment").text.strip()
                        review_dict = {}
                        review_dict['name'] = name
                        review_dict['movie'] = movie
                        review_dict['score'] = stars*20
                        review_dict['date'] = date
                        review_dict['comment'] = comment
                        
                        self.reviews.append(review_dict)
                        print(f"\t + {name}'s review n° {j+1} collected..." )
                    except AttributeError:
                        print(' - Some data is missing from the review...')
            except:
                print('Something goes wrong...')
            
        print(f'Reviews of {self.name} were obtained')
    
    
    def write_json(self):
        """
        This functions creates a JSON file for each reviewer, if it does not exists, and rewrites the file
        """
        try:
            file_path = os.path.join(self.__current_directory, self.__json_directory)
            os.makedirs(os.path.join(file_path), exist_ok=True)
            if self.reviews:
                with open(os.path.join(file_path, self.__filename), 'w') as f:
                    json.dump(self.reviews,f,indent = 4)
                print("JSON file done")
            else:
                print("No data")
        except Exception:
            print("Error writing the JSON file")

    
    
    def get_json(self):
        """
        This functions return the JSON file of the reviewer if it exists.
        """
        try:
            with open(os.path.join(self.__current_directory, self.__json_directory, self.__filename)) as f:
                data = json.load(f)
                print("Retrieving data")
                return data
        except FileNotFoundError:

            print("No data found")
            return None