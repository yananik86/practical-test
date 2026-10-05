from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Complete practical test",
        "status": "todo"
    },
    {
        "id": 2,
        "title": "Prepare presentation",
        "status": "done"
    }
]


@app.route("/tasks", methods=["GET"])
def get_tasks():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "page": page,
        "limit": limit,
        "total": len(tasks),
        "tasks": tasks[start:end]
    })


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": "todo"
    }

    tasks.append(new_task)

    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    task = next(
        (task for task in tasks if task["id"] == task_id),
        None
    )

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    data = request.get_json()

    if "status" not in data:
        return jsonify({
            "error": "Status is required"
        }), 400

    if data["status"] not in ["todo", "in_progress", "done"]:
        return jsonify({
            "error": "Invalid status"
        }), 400

    task["status"] = data["status"]

    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = next(
        (task for task in tasks if task["id"] == task_id),
        None
    )

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    tasks.remove(task)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
