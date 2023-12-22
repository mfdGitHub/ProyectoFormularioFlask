import os

class Config(object):
    SECRET_KEY = 'my_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False 
    MAIL_USE_TLS = True 
    MAIL_USERNAME = 'moyinformatico@gmail.com'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_PRUEBA')


class DevelopmentConfig(Config):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:Sup3rAdm1n..@localhost/dbflask'