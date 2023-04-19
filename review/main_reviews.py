# -*- coding: utf-8 -*-

import os
from review.reviewer import Reviewer
import json

# This functions get a list of dictionaries or read all users in the directory
# "users_json". With this it creates files of reviews of each user.
def write_all_reviews(users=[], rewrite = True):
    current_directory = os.getcwd()
    users_directory = "\\user\\users_json\\"
    list_dir = os.listdir(current_directory + users_directory)
    
    if not users:
        for file in list_dir:
            with open(current_directory + users_directory + file) as f:
                users = json.load(f)
                
                for user in users:
                    reviewer = Reviewer(user['name'], user['href'])
    
                    if rewrite:
                        reviewer.get_reviews()        
                        reviewer.write_json()
                        continue
                    
                    if not reviewer.get_json():
                        reviewer.get_reviews()        
                        reviewer.write_json()

    print("Finished")


write_all_reviews(rewrite = False)


# users = [
#     {'name':"SHEILA O'MALLEY", 'href':"https://www.metacritic.com/critic/sheila-omalley"}
#     ]
# write_all_dirs(users)