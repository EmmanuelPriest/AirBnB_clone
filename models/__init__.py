#!/usr/bin/python3

'''Magic method __init__ that powers the models package'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
