# -*- coding: utf-8 -*-

import os
from review_rotten.reviewer import Reviewer
import json

# This functions get a list of dictionaries or read all users in the directory
# "users_json". With this it creates files of reviews of each user.
def write_all_reviews(users=[], rewrite = True, append = True, check_all = False):
    current_directory = os.getcwd()
    users_directory = "\\user_rotten\\users_json\\"
    list_dir = os.listdir(current_directory + users_directory)
    
    if not users:
        for file in list_dir:
            with open(current_directory + users_directory + file) as f:
                users = json.load(f)
                
    for user in users:
        reviewer = Reviewer('paramount_plus', user['href'])
        if rewrite or not reviewer.get_json():
            reviewer.get_reviews(append = append, check_all = check_all)        
            reviewer.write_json()

    print("Finished")


write_all_reviews(rewrite = True)


# users = [
#     {'name':"SHEILA O'MALLEY", 'href':"https://www.metacritic.com/critic/sheila-omalley"}
#     ]
# write_all_dirs(users)