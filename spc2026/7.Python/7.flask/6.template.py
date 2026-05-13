from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
  user_names = ["John", "Jane", "Jim", "his", "Jack", "Jill"]
  final_html = render_template("users.html", names=user_names)
  print(final_html)
  return final_html

if __name__ == "__main__":
  app.run(debug=True)