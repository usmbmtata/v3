from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
'''from flask_login import LoginManager'''
from flask_migrate import Migrate
from flask_caching import Cache
from flask_wtf import CSRFProtect
from app.config import Config
import logging
from app import create_app
import secrets
from flask_wtf import CSRFProtect
from flask import Flask, request
from app.utils.telegram_utils import send_telegram_message

app = Flask(__name__)

app.config.from_object(Config)
SECRET_KEY = secrets.token_urlsafe(16)
csrf = CSRFProtect(app)


'''# Configure logging
log_file = 'app.log'
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
'''
 
'''login_manager = LoginManager(app)'''

# Initialize Extensions 
db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app instance
migrate = Migrate(app, db)
mail = Mail(app)
cache = Cache(app)


app = create_app()



if __name__ == '__main__':
    app.run(debug=True)
