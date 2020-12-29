import sqlite3
from flask import Flask, url_for, request, render_template

# con = sqlite3.connect('ProjectDB.db')
# print ("Opened database successfully");

# con.execute('CREATE TABLE Users (username TEXT, email TEXT, pswd TEXT)')
# print ("Table created successfully");
# con.close()

app = Flask(__name__)

# @app.route('/signup',methods = ['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         try:  
#             uname = request.form['']
#             email = request.form['email']
#             password = request.form['password']

#             with sql.connect("ProjectDB.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO Users (username, email, pswd) VALUES (?,?,?)",(uname, email, password))

#                 con.commit()
#                 msg = "Record added successfully"
#         except:
#             con.rollback()
#             msg = "Error in Inserting data"

#         finally:
#             return render_template("welcome.html")
#             con.close()


@app.route('/', methods=['POST','GET'])
def login():
    # if request.method == 'POST':
    #     user = request.form["name"]
    #     return redirect(url_for("welcome.html", name = user))
    # else:
    return render_template('login.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route("/welcome.html", methods = ["POST", "GET"])
def welcome():
    # user = request.form.get('name')
    return render_template("welcome.html", name=user)

if __name__ == "__main__":
    app.run(debug=True)