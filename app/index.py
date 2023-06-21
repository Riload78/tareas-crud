from app import app
from config import DevelopmentConfig
from utils.db import db


db.init_app(app)
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=DevelopmentConfig.DEBUG)
    app.config['TEMPLATES_AUTO_RELOAD'] = True