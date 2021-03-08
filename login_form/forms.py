from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    registered_username = StringField('registered_username', validators=[DataRequired()]) 
    password_one = StringField('password_one', validators=[DataRequired()])
    password_two = StringField('password_two', validators=[DataRequired()])    

