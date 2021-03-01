import os

class Config(object):
    #SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'BTf\xcc\xff\x06\x84#Gn\x19\x8b\x90Ig\xff'
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }