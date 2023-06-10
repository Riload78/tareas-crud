class Config():
    SECRET_KEY ='owK;zuKa{Eo79cz0KxvY[QNPX5X"~8'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER ='root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'tasks_db'
    

    
config = {
    'development':DevelopmentConfig()
}