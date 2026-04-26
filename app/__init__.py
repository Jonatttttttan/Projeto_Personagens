from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, "static", "uploads")
    app.secret_key = "Mina96####"

    # importa e regista blueprints

    from .main.routes import principal_bp

    app.register_blueprint(principal_bp)

    return app