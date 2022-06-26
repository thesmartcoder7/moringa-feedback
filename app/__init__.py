from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']  = Config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = Config.SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .main import main
    app.register_blueprint(main)

    return app

app = create_app()
    