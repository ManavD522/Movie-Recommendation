import sqlite3
from flask import Flask, url_for, request, render_template, g

app = Flask(__name__)

DATABASE = 'Desktop/Movie-Recommendation/ProjectDB.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form["name"]
        return redirect(url_for("welcome.html", name = user))
    else:
        return render_template('login.html')

@app.route("/welcome", methods = ["POST", "GET"])
def welcome():
    user = request.form.get('name')
    return render_template("welcome.html", name=user)

if __name__ == "__main__":
    app.run(debug=True)
