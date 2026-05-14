from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("form.html")

@app.route("/login", methods=["POST"])
def login():
  username = request.form["username"]
  password = request.form["password"]
  return render_template("login.html", username=username, password=password)

@app.route("/upload", methods=["POST"])
def upload():
  profile_photo = request.files["profile_photo"]
  profile_photo.save(f"static/uploads/{profile_photo.filename}")
  return render_template("upload.html", filename=profile_photo.filename)


if __name__ == "__main__":
  app.run(debug=True)