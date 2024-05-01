from flask import Blueprint, request, jsonify
from models.meal import Meal

metrics_routes = Blueprint(
    "metrics_routes", __name__, static_folder="static", template_folder="templates"
)


@metrics_routes.route("/metrics/calories", methods=["GET"])
def get_total_calories():
    meals = Meal.query.all()
    if meals:
        total_calories = 0
        for meal in meals:
            total_calories += meal.calories
        return jsonify({"total_calories": total_calories})
    return jsonify(
        {"total_calories": 0, "message": "There are no meals in the database"}
    )


@metrics_routes.route("/metrics/best-sequence", methods=["GET"])
def get_best_sequence():
    meals = Meal.query.all()
    if meals:
        best_sequence = 0
        for meal in meals:
            if meal.is_on_diet:
                best_sequence += 1
        return jsonify({"best_sequence": best_sequence})
    return jsonify({"message": "There are no meals in the database"})
