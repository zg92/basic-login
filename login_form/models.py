from login_form import app, db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'username = {User.username}, password = {User.password}'

db.create_all()
