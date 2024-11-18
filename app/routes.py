from flask import Blueprint, request, jsonify
from app.models import Task
from app.database import db

task_routes = Blueprint("tasks", __name__)

@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    new_task = Task(title=data["title"], completed=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id, "title": new_task.title, "completed": new_task.completed}), 201

@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    result = [{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks]
    return jsonify(result), 200

@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.title = data.get("title", task.title)
    task.completed = data.get("completed", task.completed)
    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "completed": task.completed}), 200

@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200
