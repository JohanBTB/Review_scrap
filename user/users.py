# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
import re
class User:
    
    
    def __init__(self, name, url='', pages=10, actual_page=0):
        self.name = name
        if url:
           self.url = url
        else:
            self.url = "https://www.metacritic.com/publication/" + re.sub(r'[^a-zA-Z0-9]', '', self.name.lower())
        self.url += "?filter=movies&page="
        
        self.users = []
        self.pages = pages
        self.actual_page = actual_page
        
        self.__json_directory = "user\\users_json"
        self.__current_directory = os.getcwd()
        self.__filename = f"users_{self.name}.json"
        
    def get_users(self, append = True, check_all = True):
        """
        This function is responsible for retrieving the information through web scraping.
        It does not perform any any writing operation
        """
        
        if append:
            try:
                with open(os.path.join(self.__current_directory, self.__json_directory, self.__filename)) as f:
                    self.users = json.load(f)
                    hrefs = set([x['href'] for x in self.users])    
            except FileNotFoundError:
                print("No file to append new data...")
                hrefs = set()

        print('Getting users...')
        
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        session.headers.update(headers)

        for j in range(self.actual_page, self.actual_page+ self.pages):
            url = self.url + f"{j}"
            print(f"Reading page {j+1}...")
            
            response = session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            try:
                scores = list(soup.find_all('ul', class_='scores'))
                if not scores:
                    print("No more pages found")
                    break
                for i, score in enumerate(scores):
                    user = {}
                    try:
                        span = list(score.find_all('span'))[-1].find('a')
                        href = "https://www.metacritic.com" + span.get('href')
                        name = span.text
                        if href in hrefs:
                            if not check_all: 
                                print("This point has already been checked, closing execution...")
                                break 
                            print(f"\tUser {name} have been already accepted.")
                            continue
                        
                        hrefs.add(href)
                        name = span.text
                        user['name'] = name
                        user['href'] = href
                        self.users.append(user)
                        print(f"\tUser {i} accepted")
                    except Exception as e:
                        print(f"\tNo enough data. Omitting user {i}...")
                        # print(e)
                        continue
            except:
                print("No webpage url was found. The iteration was stopped abruptly...")
                break
        print(f'Users of the webpage {self.name} were obtained.')
    
    
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