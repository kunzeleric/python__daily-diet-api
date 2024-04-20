from flask import request, jsonify, Blueprint
from models.user import User
from database import db
from flask_login import login_user, logout_user, login_required, current_user

user_routes = Blueprint(
    "user_routes", __name__, static_folder="static", template_folder="templates"
)


# Create a new user route
@user_routes.route("/register", methods=["POST"])
def register_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Registered successfully!"}), 200

    return jsonify({"message": "Error creating user, please validate your data."}), 400


# Login Route
@user_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return jsonify({"message": "Logged in successfully!"}), 200
        else:
            return jsonify({"message": "Credentials are invalid!"}), 400


# Logout Route
@user_routes.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200
