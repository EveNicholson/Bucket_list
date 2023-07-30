from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/destinations_app"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from controllers.destination_controllers import destinations_blueprint
app.register_blueprint(destinations_blueprint)