# -*- coding: utf-8 -*-

from user.users import User
"""
# Retrieving data form rogerEbert
"""
# user = User("RogerEbert.com", "https://www.metacritic.com/publication/rogerebertcom?filter=movies&page=") # Max 191


"""
# Retrieving data from Indiewire
"""
user = User("Indiwire", "https://www.metacritic.com/publication/indiewire?filter=movies&page=",pages = 150)

user.get_users(append = True, check_all=True)
user.write_json()