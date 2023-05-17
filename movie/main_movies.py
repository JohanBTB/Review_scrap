# -*- coding: utf-8 -*-

from movie.movier import Movier
import os
import json

# This functions get a list of dictionaries or read all movies in the directory
# "webs_json". With this it creates files of movies of each user.
def write_all_movies(users=[], rewrite = True, append = True, check_all = False):

    current_directory = os.getcwd()
    users_directory = "\\user\\users_json\\"
    list_dir = os.listdir(current_directory+ users_directory)
    
    if not users:
        # for file in list_dir:
        for file in ['users_RogerEbert.com.json']:
            with open(os.path.join(current_directory + users_directory, file)) as f:
                print(f"Processing file {file}...")
                users = json.load(f)
                
    for user in users:
        movier = Movier(user['name'])
        if rewrite or not movier.get_json():
            movier.get_movies(append = append, check_all=check_all)        
            movier.write_json()
            print(f"{user['name']} processed...")
            continue
                    
        
    print("Finished")    



# write_all_movies([{'name':"SHEILA O'MALLEY"}])
write_all_movies(check_all = True)

"""
This lines are to get json file of the users
"""
   
 
