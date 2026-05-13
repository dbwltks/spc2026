from flask import Flask, render_template, request
import os
app = Flask(__name__)

# 저장소 설정
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def allowed_file(filename):
  ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
  # 실서비스에서는 파일명을 중복되지 않게 해야 함
  profile_photo = request.files["profile_photo"]
  profile_photo.save(f"{app.config['UPLOAD_FOLDER']}/{profile_photo.filename}")

  return f"파일 업로드 성공: {profile_photo.filename}"


if __name__ == "__main__":
  app.run(debug=True)