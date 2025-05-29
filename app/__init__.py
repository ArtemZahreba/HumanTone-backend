from flask import Flask
from app.routes import bp
from app.config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(bp)

    CORS(app)
    return app