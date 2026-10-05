from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Данные не переданы"}), 400

    email = data.get("email")
    birth_date = data.get("birthDate")

    if not email:
        return jsonify({"error": "Введите email"}), 400

    if "@" not in email:
        return jsonify({"error": "Введите корректный email"}), 400

    if not birth_date:
        return jsonify({"error": "Введите дату рождения"}), 400

    return jsonify({
        "message": "Регистрация прошла успешно",
        "email": email,
        "birthDate": birth_date
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
