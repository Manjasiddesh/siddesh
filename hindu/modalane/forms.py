from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    email = StringField('   email',validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    #email= StringField('email', validators=[InputRequired()])

