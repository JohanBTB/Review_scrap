# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import json
import os

class Reviewer:

    
    def __init__(self, name, url, pages=10, actual_page=0):
        self.name = name
        if url:
            self.url = url
        else:
            self.url = self.name.lower().replace(' ', '-').replace("'", '')
        self.url += "?page="
        self.pages = pages
        self.actual_page = actual_page
        self.reviews = []
        self.__json_directory = "\\review\\reviews_json"
        self.__current_directory = os.getcwd()
        
    
    def get_json_directory(self):
        return self.__json_directory
    
    def get_current_directory(self):
        return self.__current_directory
    
    def get_reviews(self):
        """
        This function is responsible for retrieving the information through web scraping.
        It does not perform any any writing operation

        """
        
        print('Getting reviews...')
        for j in range(self.actual_page, self.actual_page+ self.pages):
            url = self.url + f"{j}"
            print(f"Reading page {j+1}...")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            try:
                review_contents = list(soup.find('ol', class_='reviews').find_all('div', class_='review_content'))
                for i in range(len(review_contents)):
                    content = review_contents[i]
                    try:
                        score = content.find('li', class_='brief_critscore').span.text
                        href = 'https://www.metacritic.com' + content.find('div', class_='review_product').find('a').get('href')
                        movie = content.find('div', class_='review_product').find('a').text
                        review={
                            'name':self.name,
                            'movie':movie,
                            'score':score,
                            'href':href
                            }
                        self.reviews.append(review)
                        print(f"\tReview {i} accepted")
                        
                    except Exception:
                        print(f"\tNo enough data. Omitting review {i}...")
            except:
                print("No webpage url was found. The iteration was stopped abruptly...")
                break
        print(f'Reviews of {self.name} were obtained')
    
    
    def write_json(self):
        """
        This functions creates a JSON file for each reviewer, if it does not exists, and rewrites the file
        """

        if not os.path.exists(self.__current_directory + self.__json_directory):
            os.makedirs(self.__json_directory)
            
        if self.reviews:
            with open(f"{self.__current_directory + self.__json_directory}\\reviews_{self.name}.json", "w") as f:
                json.dump(self.reviews, f, indent=4)
            print('JSON file done')
        else:
            print('No data')
    
    
    def get_json(self):
        """
        This functions return the JSON file of the reviewer if it exists.
        """
        try:
            with open(f"{self.__current_directory + self.__json_directory}\\reviews_{self.name}.json") as f:
                data = json.load(f)
                print("Retrieving data")
                return data
        except FileNotFoundError:
            print("No data found")