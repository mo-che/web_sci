# -*- coding: utf-8 -*-

"""
    this code for setup database, Its'll call when setup.sh run
"""
import os
import json
from collections import defaultdict
from django.core.files import File
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from app.models import Task

User = get_user_model()

print()
print('='*40)
_secret_path = os.path.join('secret','setup.json')
print("-- Read secret configuration --")
try:
    with open(_secret_path, 'r') as fp:
        secret_var = json.load(fp)
except FileNotFoundError as err:
    print('********************************************')
    print('!!! Secret File Not Found, use default value')
    print('********************************************')
    secret_var = {
        'admin_email': '',
        'admin_username': 'admin',
        'admin_password': 'qwer1234'
    }
    for k, v in secret_var.items():
        print('\t{}: {}'.format(k, v))
secret_var = defaultdict(str, secret_var)
print()

print("- Create Default Group -")
mechanic_group = Group.objects.create(name="mechanic")
print()

print("- Create Admin user")
admin = User.objects.create_superuser(
    username=secret_var['admin_username'],
    password=secret_var['admin_password'],
    email=secret_var['admin_email'],
)

user = User.objects.create_user(
    username='user01',
    password='qwer1234'
)

mechanic = User.objects.create_user(
    username='mec01',
    password='qwer1234'
)
mechanic_group.user_set.add( mechanic )
print()

kwargs = {'title': 'ghghgh', 
    'description': 'fgfgfhfhghg', 
    'building': 'LC 5', 
    'floor': '1', 
    'room': '100',
    'requester': user,
} 
Task.objects.create( **kwargs)