from flask import Flask, render_template
from backend.queries import onequery

app = Flask(__name__)

@app.route("/")
def main():
    data = onequery() 
    return render_template('home.html', data = data )

if __name__ == "__main__":
    app.run()
