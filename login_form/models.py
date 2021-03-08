from login_form import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'username = {self.username}, password = {self.password}'

# db.drop_all()
# db.create_all()