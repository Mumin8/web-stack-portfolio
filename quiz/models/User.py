from sqlalchemy.sql import func
from quiz import db, login_manager, app
from flask_login import UserMixin



@login_manager.user_loader
def loader_user(user_id):
    return Student.query.get(user_id)

class Student(db.Model, UserMixin):
    '''
    the student model definition
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Student {self.username}>'
    


class Quiz(db.Model):
    '''
    The quiz model definition
    '''
    
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(20), nullable=True, default='0')
    def update(self, result):
        self.result = result
        db.session.commit()

    def __repr__(self):
        return f'<Quiz {self.result}>'
    