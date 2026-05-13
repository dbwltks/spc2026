from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search")
def search():
  query = request.args.get("q")
  page = request.args.get("page", "1")

  user_input = f"Search keyword: {query}, Page: {page}"

  print(user_input)
  return jsonify({"message": user_input})


@app.route("/user/<username>/post")
def get_user_posts(username):
  page = request.args.get("page", default=1, type=int)
  result = f"User: {username}, Page: {page}"
  print(result)
  return jsonify({"message": result})

@app.route("/users")
def search_user():
  name = request.args.get("name")
  age = request.args.get("age")
  result = f"Name: {name}, Age: {age}"
  print(result)
  return jsonify({"message": result})

if __name__ == "__main__":
  app.run(debug=True)