from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

# Crie as instâncias do Flask, SQLAlchemy e LoginManager
app = Flask(__name__)

from datetime import timedelta

app.permanent_session_lifetime = timedelta(hours=48)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-blog-4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'
UPLOAD_FOLDER = 'app/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)



# Importe e registre as blueprints (rotas) da sua aplicação
from app.routes import artigos_bp, comments_bp, admin_bp
app.register_blueprint(artigos_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(admin_bp)