#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
from apoc.models import User

def hash_password(password):
    return hashlib.md5(password).hexdigest()

def get_token(user_id):
    salt_water = '@@' + str(int(user_id) * 2) + '@@'
    
    return hashlib.md5(salt_water).hexdigest()

def is_login(request):
    user_id = request.get_cookie('__user_id')
    token   = request.get_cookie('__token')

    return token == get_token(user_id) if user_id and token else False

def seed_cookies(request, user_id):
    request.set_cookie('__user_id', user_id)
    request.set_cookie('__token', get_token(user_id))
    
def get_user(request, db_session):
    if (is_login(request)):
        user_id = request.get_cookie('__user_id')
        return User.get(db_session, user_id)
    else:
        return None

def logout(request):
    request.set_cookie('__user_id', '')
    request.set_cookie('__token', '')
