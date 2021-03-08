from flask import render_template, request, redirect, flash
from login_form import app
from login_form.models import User
from login_form.forms import LoginForm, RegisterForm

@app.route('/', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            print(request.form['login'], request.form['password'])
            user = User.query.filter_by(username=request.form['login']).first()
            print(user)
            # if user.username == request.form['login'] and user.password == request.form['password']:
            #     print('you are logged in!')
            # else:
            #     print('sorry that username or password does not match')
        if request.form['btn'] == 'Register':
            if request.form['password-first'] == request.form['password-second']:
                registered_user = User(username=request.form['create-username'], password = request.form['password-first'])
                User.session.add(registered_user)
                print(request.form['password-second'], request.form['password-first'])
                print(User.query.all())
            else:
                print('Please make sure your passwords match!')
    return render_template('index.html', login_form = login_form, registered_form = register_form)
