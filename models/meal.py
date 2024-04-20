from database import db
import datetime


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    is_on_diet = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "meal_name": self.meal_name,
            "description": self.description,
            "date_time": self.date_time,
            "is_on_diet": self.is_on_diet,
            "user_id": self.user_id,
        }
