from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():
  return "hello phong le"

print(__name__)
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)