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
        self.url += "?page="
        
        self.users = []
        self.pages = pages
        self.actual_page = actual_page
        
    def get_users(self):
        print('Getting users...')
        hrefs = set()
        for j in range(self.actual_page, self.actual_page+ self.pages):
            url = self.url + f"{j}"
            print(f"Reading page {j+1}...")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            try:
                scores = list(soup.find_all('ul', class_='scores'))
                    
                for i in range(len(scores)):
                    score = scores[i]
                    user = {}
                    try:
                        span = list(score.find_all('span'))[-1].find('a')
                        href = span.get('href')
                        if href in hrefs:
                            print(f"\tUser {i} have been already accepted.")
                            continue
                        hrefs.add(href)
                        name = span.text
                        user['name'] = name
                        user['href'] = "https://www.metacritic.com" + href
                        self.users.append(user)
                        print(f"\tUser {i} accepted")
                    except Exception:
                        print(f"\tNo enough data. Omitting user {i}...")
                        break
            except:
                print("No webpage url was found. The iteration was stopped abruptly...")
                break
        print(f'Users of the webpage {self.name} were obtained.')
    
    def write_json(self):
        json_directory = "\\users_json"
        current_directory = os.getcwd()
        
        if not os.path.exists(current_directory + json_directory):
            os.makedirs(json_directory)
            
        if self.users:
            with open(f"{current_directory + json_directory}\\{self.name}", "w") as f:
                json.dump(self.users, f, indent=4)
            print('JSON file done')
        else:
            print('No data')
