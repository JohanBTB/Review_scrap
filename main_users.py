# -*- coding: utf-8 -*-

from user import User

user = User("RogerEbert.com", "https://www.metacritic.com/publication/rogerebertcom?page=")

user.get_users()

user.write_json()