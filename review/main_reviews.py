# -*- coding: utf-8 -*-

import os
from review.reviewer import Reviewer
import json

# This functions get a list of dictionaries or read all users in the directory
# "users_json". With this it creates files of reviews of each user.
def write_all_reviews(users=[], rewrite = True, append = True, check_all = True):
    current_directory = os.getcwd()
    users_directory = "\\user\\users_json\\"
    list_dir = os.listdir(current_directory + users_directory)
    
    if not users:
        # for file in list_dir:
        for file in ['users_Indiwire.json']:
            with open(current_directory + users_directory + file) as f:
                users.extend(json.load(f))
    print(users)
    for user in users:
        # print(type(user))
        reviewer = Reviewer(user['name'], user['href'])

        if rewrite or not reviewer.get_json():
            reviewer.get_reviews(append = append, check_all = check_all)        
            reviewer.write_json()
            continue
                    
    print("Finished")


write_all_reviews(rewrite = True)


# users = [
#     {'name':"SHEILA O'MALLEY", 'href':"https://www.metacritic.com/critic/sheila-omalley"}
#     ]
# write_all_dirs(users)