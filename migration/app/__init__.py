from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '96832c3f32b9a586095cf19384a9cccd1d51c9683f6e2239979d258cb975ba4f'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LcaaZkUAAAAAAX5Ff8gbbKglzAvHl31A7pbVYbM"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LcaaZkUAAAAADUqadT2yzMA0mHD_m0h48D_aVMg"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

from app import routes
