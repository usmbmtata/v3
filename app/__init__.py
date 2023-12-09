from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_mail import Mail
from config import Config

import datetime

# Initialize SQLAlchemy for database connection
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    # Initialize the database
    sess = Session()
    sess.init_app(app)
    db.init_app(app)

    from app.views.auth import auth_bp
    from app.views.dashboard import dashboard_bp
    from app.views.index import index_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(index_bp)

    return app