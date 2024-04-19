from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from database import db
from models.user import User
from routes.user.routes import user_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = "S2@#!4S1WSA1SS#@#$12311#@!#!@"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"

# DB initialization
db.init_app(app)

# Login config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Register user route blueprint
app.register_blueprint(user_routes)

# Callback function to reload user object from user ID stored in session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/", methods=["GET"])
def health_status():
    return "API online!"

if __name__ == "__main__":
    app.run(debug=True)