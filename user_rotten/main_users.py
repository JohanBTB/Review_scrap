# -*- coding: utf-8 -*-

from user_rotten.users import User


user = User('paramount_plus',  min_reviews=5)
user.get_users()
user.write_json()
