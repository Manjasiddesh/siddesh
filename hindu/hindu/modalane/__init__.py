from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask import render_template,request,flash,redirect,url_for
from .forms import LoginForm

from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
class uinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name,email, password):
        self.name = name
        self.email = email
        self.password = password




@app.route('/')
def index():
     return render_template("index.html")


@app.route('/contact')
def contact():
     return render_template("contact.html")


@app.route('/about')
def about():
     return render_template("about.html")


@app.route('/signup')
def signup():
     return render_template("signup.html")


@app.route('/signup',methods=['POST'])
def signup_post():
     name = request.form.get('name')
     email = request.form.get('email')
     password = request.form.get('password')
     check = uinfo.query.filter_by(email=email).first()
     if check:
          print("user already exists")
          return redirect(url_for("signup"))
     new_user = uinfo(name,email,password)
     db.session.add(new_user)
     db.session.commit()
     return redirect(url_for("login"))


@app.route('/login',methods=['GET','POST'])
def login():
     lform = LoginForm()
     if lform.validate_on_submit():
          verifying = uinfo.query.all()
          for veri in verifying:
              if request.form['email'] != veri.email or request.form['password'] != veri.password:
                  continue
              else:
                  display = veri.name
                  return render_template("contact.html", data=display)
          flash("invalid credential. please try again")
     return render_template("login.html",title = "Login",form=lform)
migrate = Migrate(app,db)


