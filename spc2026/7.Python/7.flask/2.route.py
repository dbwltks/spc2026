from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello, World!"

@app.route("/about")
def about():
  return "About Page"

@app.route("/user/<username>")
def user(username):
  return f"Hello, {username}!"

@app.route("/admin")
def admin():
  return "Admin Page"

if __name__ == "__main__":
  app.run(debug=True)