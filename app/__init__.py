from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy # Conexão SQL

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "auth.login" # rota de login

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, "static", "uploads")
    app.secret_key = "Mina96####"

    # Conexão postgres
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mina96#@localhost:5432/meus_personagens' # string de conexão
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager.init_app(app)

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    # importa e regista blueprints

    from .main.routes import principal_bp

    app.register_blueprint(principal_bp)

    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app