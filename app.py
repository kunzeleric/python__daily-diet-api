from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from database import db
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = "S2@#!4S1WSA1SS#@#$12311#@!#!@"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"

# DB initialization
db.init_app(app)
# Login config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Callback function to reload user object from user ID stored in session
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Login Route
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data.username and data.password:
        user = User.query.filter_by(username=data.username).first()
        if user and user.check_password(data.password):
            login_user(user)
            return jsonify({ "message": "Logged in successfully!" }), 200
        else:
            return jsonify({ "message": "Credentials are invalid!" }), 400

# Logout Route
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({ "message": "Logged out successfully!" }), 200

@app.route("/", methods=["GET"])
def health_status():
    return "API online!"

if __name__ == "__main__":
    app.run(debug=True)