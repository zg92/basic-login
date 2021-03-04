from flask import Flask, render_template, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

db.create_all()

def __repr__(self):
    return f'username = {username}, password = {password}'

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            print(request.form['login'], request.form['password'])
            user = User.query.filter_by(username=request.form['login']).first()
            print(user)
            if user.username == request.form['login'] and user.password == request.form['password']:
                print('you are logged in!')
            else:
                print('sorry that username or password does not match')
        if request.form['btn'] == 'Register':
            if request.form['password-first'] == request.form['password-second']:
                registered_user = User(username=request.form['create-username'], password = request.form['password-first'])
                db.session.add(registered_user)
                print(request.form['password-second'], request.form['password-first'])
                print(User.query.all())
            else:
                print('Please make sure your passwords match!')
    return render_template('index.html')


app.run(debug=True)