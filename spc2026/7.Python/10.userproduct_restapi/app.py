from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = [
  {"id": 1, "name": "John", "age": 30, "phone": "010-1234-5678"},
  {"id": 2, "name": "Jane", "age": 25, "phone": "010-1234-5679"},
  {"id": 3, "name": "Jim", "age": 35, "phone": "010-1234-5680"},
  {"id": 4, "name": "his", "age": 28, "phone": "010-1234-5681"},
  {"id": 5, "name": "Jack", "age": 32, "phone": "010-1234-5682"},
  {"id": 6, "name": "Jill", "age": 28, "phone": "010-1234-5683"},
]

# 정적 사이트 라우팅
@app.route("/")
def index():
  # user_name = request.args.get("name")
  # user_age = request.args.get("age")
  # user_phone = request.args.get("phone")
  return render_template("index.html")

# @app.route("/user")
# def get_user():
#   return render_template("user.html")

# @app.route("/user/<int:user_id>")
# def get_user_by_id(user_id):
#   return jsonify({"user": users[user_id]})

# @app.route("/user", methods=["POST"])
# def create_user():
#   return jsonify({"user": users[len(users)]})

# # API 라우팅
# @app.route("/api/user/<int:user_id>")
# def get_user_by_id_api(user_id):
#   return jsonify({"user": [u for u in users if u["id"] == user_id]})
  
# @app.route("/api/product/")
# def get_product():
#   return jsonify({"product": product})

if __name__ == "__main__":
  app.run(debug=True)