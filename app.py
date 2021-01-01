import warnings
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


@app.route("/welcome", methods = ["GET"])
@login_required
def welcome():
    return render_template("welcome.html", user = current_user.username)

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

