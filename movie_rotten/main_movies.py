# -*- coding: utf-8 -*-

from movie_rotten.movier import Movier
import os
import json

# This functions get a list of dictionaries or read all movies in the directory
# "webs_json". With this it creates files of movies of each user.
def write_all_movies(affiliates=[], rewrite = True):
                
    for affiliate in affiliates:
        movier = Movier(affiliate, f"https://www.rottentomatoes.com/browse/movies_at_home/affiliates:{affiliate}")
        # if rewrite or not movier.get_json():
        #     movier.get_movies()        
        #     movier.write_json()
        #     print(f"{affiliate} processed...")
        #     continue
        movier.get_movies()        
        movier.write_json()
    print("Finished")    



# write_all_movies([{'name':"SHEILA O'MALLEY"}])
write_all_movies(['paramount_plus'])

"""
This lines are to get json file of the users
"""

#https://www.rottentomatoes.com/critics/source/1708 rogerbert
