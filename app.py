from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "S2@#!4S1WSA1SS#@#$12311#@!#!@"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"

db.init_app(app)

@app.route("/", methods=["GET"])
def health_status():
    return "API online!"

if __name__ == "__main__":
    app.run(debug=True)