from flask import Flask
from app.routes import task_routes
from app.database import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)

app.register_blueprint(task_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
