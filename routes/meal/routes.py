from flask import request, jsonify, Blueprint
from models.meal import Meal
from database import db
from flask_login import login_required, current_user
from datetime import datetime

meal_routes = Blueprint(
    "meal_routes", __name__, static_folder="static", template_folder="templates"
)


@meal_routes.route("/meal/register", methods=["POST"])
@login_required
def create_meal():
    data = request.json
    meal_name = data.get("meal_name")
    description = data.get("description")
    is_on_diet = data.get("is_on_diet", False)
    user_id = current_user.id
    if meal_name and description:
        diet = Meal(
            meal_name=meal_name,
            description=description,
            user_id=user_id,
            is_on_diet=is_on_diet,
        )
        db.session.add(diet)
        db.session.commit()
        return jsonify({"message": "Meal created successfully!"}), 200
    return jsonify({"message": "Error creating meal, please validate your data."}), 400


@meal_routes.route("/meal", methods=["GET"])
@login_required
def fetch_meals():
    user_id = current_user.id
    meals = Meal.query.filter_by(user_id=user_id).all()
    if meals:
        meals_list = [meal.to_dict() for meal in meals]
        return jsonify({"meals": meals_list}), 200
    return jsonify({"message": "No meals found for this user."}), 404


@meal_routes.route("/meal/<int:id>", methods=["GET"])
@login_required
def fetch_meal(id):
    meal = Meal.query.filter_by(id=id, user_id=current_user.id).first()
    if meal:
        return jsonify({"meal": meal.to_dict()}), 200
    return jsonify({"message": "Meal not found."}), 404


@meal_routes.route("/meal/<int:id>", methods=["PUT"])
@login_required
def update_meal(id):
    meal = Meal.query.filter_by(id=id, user_id=current_user.id).first()
    if meal:
        data = request.json
        meal_name = data.get("meal_name", meal.meal_name)
        description = data.get("description", meal.description)
        is_on_diet = data.get("is_on_diet", meal.is_on_diet)
        meal.meal_name = meal_name
        meal.description = description
        meal.is_on_diet = is_on_diet
        meal.date_time = datetime.now()
        
        db.session.commit()
        return jsonify({"message": "Meal updated successfully!"}), 200
    return jsonify({"message": "Meal not found."}), 404
