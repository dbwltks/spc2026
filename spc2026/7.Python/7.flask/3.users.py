from flask import Flask, jsonify

app = Flask(__name__)

users = [
  {"name": "John", "age": 30, "phone": "010-1234-5678"},
  {"name": "Jane", "age": 25, "phone": "010-1234-5679"},
  {"name": "Jim", "age": 35, "phone": "010-1234-5680"},
  {"name": "his", "age": 28, "phone": "010-1234-5681"},
  {"name": "Jack", "age": 32, "phone": "010-1234-5682"},
  {"name": "Jill", "age": 28, "phone": "010-1234-5683"},
]

# 파이썬의 리스트 폼, 각각의 리스트에는 딕셔너리

@app.route("/")
def home():
  return jsonify({"users": users})

@app.route("/users/<name>")
def get_user_by_name(name):
  print("사용자 이름: ", name)
  user = None

  for u in users:
    if u["name"] == name:
      user = u
  
  if user:
    return jsonify({"user": user})
  else:
    return jsonify({"error": "사용자를 찾을 수 없습니다."}), 404

@app.route("/users/<int:age>")
def get_user_by_age(age):
  print("사용자 나이: ", age)
  user = []
  
  for u in user:
    if u["age"] == age:
      user = [*user, u]
  
  return jsonify({"user": user})

if __name__ == "__main__":
  app.run(debug=True)