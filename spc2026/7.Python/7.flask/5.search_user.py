from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
  {"name": "John", "age": "30", "phone": "010-1234-5678"},
  {"name": "Jane", "age": "25", "phone": "010-1234-5679"},
  {"name": "Jim", "age": "35", "phone": "010-1234-5680"},
  {"name": "his", "age": "28", "phone": "010-1234-5681"},
  {"name": "Jack", "age": "32", "phone": "010-1234-5682"},
  {"name": "Jill", "age": "28", "phone": "010-1234-5683"},
]

@app.route("/search")
def search_user():
  result = None
  name = request.args.get("name")
  age = request.args.get("age")
  phone = request.args.get("phone")

  result = None

  for u in users:
    if name and u["name"] == name:
      result = u
    if age and u["age"] == age:
      result = u
    if phone and u["phone"] == phone:
      result = u
  if result:
    return jsonify({"message": result})
  else:
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
  app.run(debug=True)