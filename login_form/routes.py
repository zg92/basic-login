from flask import render_template, request, redirect, flash
from login_form import app, db
from login_form.models import User
from login_form.forms import LoginForm, RegisterForm
from login_form import bcrypt

@app.route('/', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            print('success!')
    else:
        flash('Login Unsuccessful. Please check email and password', 'danger')
    if request.method == 'POST':
        if register_form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(register_form.password_one.data).decode('utf-8')
            user = User(username=register_form.registered_username.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account Created! Please login to continue!', 'success')
    return render_template('index.html', login_form = login_form, register_form = register_form)
