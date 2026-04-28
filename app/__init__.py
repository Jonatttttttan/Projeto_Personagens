from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy # Conexão SQL

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, "static", "uploads")
    app.secret_key = "Mina96####"

    # Conexão postgres
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mina96#@localhost:5432/meus_personagens' # string de conexão
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    # importa e regista blueprints

    from .main.routes import principal_bp

    app.register_blueprint(principal_bp)

    return app