# -*- coding: utf-8 -*-

from movier import Movier
import os
import json

# This functions get a list of dictionaries or read all movies in the directory
# "webs_json". With this it creates files of movies of each user.
def write_all_movies(users=[]):
    current_directory = os.getcwd()
    users_directory = "\\users_json\\"
    list_dir = os.listdir(current_directory + users_directory)
    
    if not users:
        for file in list_dir:
            with open(current_directory + users_directory + file) as f:
                users = json.load(f)
                
    for user in users:
        movier = Movier(user['name'])
        movier.get_movies()        
        movier.write_json()
        # print(f"User {user['name']} 100% compelte...")
        
    print("Finished")

# write_all_movies([{'name':"SHEILA O'MALLEY"}])

write_all_movies()
   
    

