from flask import Flask, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(app)

class Login(db.Model):
    email = db.Column(db.String(50), primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.email

@app.route('/', methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route("/welcome", methods = ["POST"])
def welcome():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    new_user = Login(email = email, username = username, password = password)
    
    try:
        if("" in [email, username, password]):
            return render_template("error.html")
        db.session.add(new_user)    
        return render_template("welcome.html", username=username)
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)

