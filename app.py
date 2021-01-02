import warnings
import json
from flask import Flask, url_for, request, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisasecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

input_movies = ["TERMINATOR 3", "BAD BOYS II", "CHRONICLES OF THE NARNIA", "S.W.A.T.", "35 UP", "JOHNY ENGLISH", "KUNG FU PANDA", "PULP FICTION", "HARRY POTTER", "BABY'S DAY OUT", "COBRA", "THE PRESTIGE", "HAPPT FEET", "DELHI BELLY", "CARS 2", "THE SMURFS", "THE AVENGERS", "ENGLISH VINGLISH", "TAKEN", "PARANORMAL ACTIVITY", "WOLVERINE", "LONE RANGER", "THE HOBBIT", "FINAL DESTINATION"]
movie_id = [6537, 6548, 41566, 6595, 26712, 6550, 59784, 296, 4896, 5096, 6800, 48780, 49274, 88069, 87876, 88356, 122912, 99636, 96861, 97701, 103772, 103384, 106489, 71252]

class Login(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid Email"), Length(max = 50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max = 80)])

class SignupForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid Email"), Length(max = 50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])

@app.route('/', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Login.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                return redirect(url_for('welcome'))
        return '<h1>Invalid Username or password</h1>'

    if request.method == "GET":
        return render_template('login.html', form = form)

@app.route('/signup', methods=['POST','GET'])
def signup():
    form = SignupForm()
    
    if form.validate_on_submit():
        secure_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Login(email = form.email.data, username = form.username.data, password = secure_password)
        try: 
            db.session.add(new_user)
            db.session.commit()
        except:
            pass
        return redirect(url_for('welcome'))
        # return '<h1>New user has  been created!</h1>'

    if request.method == "GET":
        return render_template('signup.html', form = form)


@app.route("/welcome", methods = ["GET", "POST"])
@login_required
def welcome(input_field=""):
    if request.method == "POST":
        input_field = request.json['data']
        print(input_field)
        return "<h1>Data Passed</h1>"
    return render_template("welcome.html", user = current_user.username, movies = input_movies, mid = movie_id)

@app.route("/logout", methods = ["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("signup"))

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)

