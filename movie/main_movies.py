# -*- coding: utf-8 -*-

from movie.movier import Movier
import os
import json

# This functions get a list of dictionaries or read all movies in the directory
# "webs_json". With this it creates files of movies of each user.
def write_all_movies(users=[], rewrite = True):
    """
    

    Parameters
    ----------
    users : TYPE, optional
        DESCRIPTION. The default is [].
    rewrite : TYPE, boolean
        DESCRIPTION. The default is True.

    Returns 
    -------
    None.

    """
    current_directory = os.getcwd()
    users_directory = "\\user\\users_json\\"
    list_dir = os.listdir(current_directory + users_directory)
    
    if not users:
        # for file in list_dir:
        for file in ['users_RogerEbert.com.json']:
            with open(os.path.join(current_directory, users_directory, file) as f:
                print(f"Processing file {file}...")
                users = json.load(f)
                
                for user in users:
                    movier = Movier(user['name'])
                    if rewrite or not movier.get_json():
                        movier.get_movies()        
                        movier.write_json()
                        print(f"{user['name']} processed...")
                        continue
                    
        
        
        # print(f"User {user['name']} 100% compelte...")
        
    print("Finished")    

"""
This first lines are to create json file of all the users
"""

# write_all_movies([{'name':"SHEILA O'MALLEY"}])
write_all_movies()

"""
This lines are to get json file of the users
"""
   
 
