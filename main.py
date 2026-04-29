from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return "Python backend is working!"
@app.route("/blog")
def block():
    return "Hello welcome"

if __name__ == "__main__":
    app.run(debug=True)
