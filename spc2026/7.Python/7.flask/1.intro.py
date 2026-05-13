# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return """
  <html>
    <head>
      <title>나의 홈페이지</title>
    </head>
    <body>
      <h1>Hello, World!</h1>
      <p>나의 홈페이지에 오신 것을 환영합니다.</p>
      <p>나의 홈페이지에 오신 것을 환영합니다.</p>
      <p>나의 홈페이지에 오신 것을 환영합니다.</p>
    </body>
  </html>
  """

if __name__ == "__main__":
  app.run(debug=True)

