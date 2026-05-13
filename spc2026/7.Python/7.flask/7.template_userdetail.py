from flask import Flask, render_template

app = Flask(__name__)

users = [
  {"name": "홍길동", "age": 30, "phone": "010-1234-5678"},
  {"name": "이순신", "age": 25, "phone": "010-1234-5679"},
  {"name": "강감찬", "age": 35, "phone": "010-1234-5680"},
  {"name": "을지문덕", "age": 28, "phone": "010-1234-5681"},
  {"name": "유관순", "age": 32, "phone": "010-1234-5682"},
  {"name": "이성계", "age": 28, "phone": "010-1234-5683"},
]

@app.route("/")
def index():
  return render_template("users_detail.html", users=users)
  print(final_html)

if __name__ == "__main__":
  app.run(debug=True)