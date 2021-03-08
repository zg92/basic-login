from flask_wtf import FlaskForm
from login_form.models import User
from wtforms import StringField, PasswordField, ValidationError, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    submit_login = SubmitField('Login')

class RegisterForm(FlaskForm):
    registered_username = StringField('registered_username', validators=[DataRequired()]) 
    password_one = PasswordField('password_one', validators=[DataRequired()])
    password_two = PasswordField('password_two', validators=[DataRequired(), EqualTo('password_one')]) 
    register_login = SubmitField('Register')

    def validate_username(self, registered_username):
        user = User.query.filter_by(username=registered_username.data).first()
        if user:
            raise ValidationError('That username exists. Please choose a different username.')
