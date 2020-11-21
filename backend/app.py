from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def run_app():
    return render_template("index.html", **{"greeting": "Hello from Flask!"})

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8000)