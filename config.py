import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/avengers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    UPLOAD_FOLDER = r'uploads'
    ALLOWED_EXTENSIONS = ('json', 'xml', 'txt', 'csv')
