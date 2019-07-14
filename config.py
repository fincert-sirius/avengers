import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

    UPLOAD_FOLDER = '/uploads'
    ALLOWED_EXTENSIONS = ('json', 'xml', 'txt', 'csv')
