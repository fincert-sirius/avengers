import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    UPLOAD_FOLDER = r'C:\Users\User\PycharmProjects\avengers_final\uploads'
    ALLOWED_EXTENSIONS = ('json', 'xml', 'txt', 'csv')
