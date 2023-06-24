import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KET')
    MAIL_SERVER =  os.environ.get('MAIL_SERVER')
    MAIL_PORT =  os.environ.get('MAIL_PORT')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER ='root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'tasks_db'
    

    
config = {
    'development':DevelopmentConfig()
}