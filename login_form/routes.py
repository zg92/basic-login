from flask import render_template, request, redirect, flash, url_for
from login_form import app, db
from login_form.models import User
from login_form.forms import LoginForm, RegisterForm
from login_form import bcrypt
from flask_login import login_user, current_user


@app.route('/', methods=['POST','GET'])
def login():

    # forms from forms.py
    login_f = LoginForm()
    register_f = RegisterForm()

    # login logic
    if login_f.validate_on_submit():
        user = User.query.filter_by(username=login_f.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_f.password.data):
            login_user(user)
            return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')

    # registration logic
    if request.method == 'POST':
        if register_f.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(
                register_f.password_one.data).decode('utf-8')
            user = User(username=register_f.registered_username.data,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account Created! Please login to continue!', 'success')

    return render_template('index.html', login_form=login_f, register_form=register_f)

@app.route('/home')
def home():

    # message for logged in user
    if current_user.is_authenticated:
        flash(f'Welcome {current_user.username.title()}! Now you can see secret content!', 'success')
    else:
        return redirect(url_for('login'))

    return render_template('home.html')
