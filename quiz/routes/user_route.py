from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user
from quiz import app, db
from quiz.models.User import Student
from .Quiz import start_quiz


@app.route('/register/', methods=('GET', 'POST'))
def register():
    '''
    The student registration route
    '''
    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        student = Student(
            username=username,
            email=email,
            password=password
        )
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    the student login route
    '''

    if request.method == "POST":
        username = request.form.get("username")
        student = Student.query.filter_by(username=username).first()
        if student.password == request.form.get("password"):
            login_user(student)
            return redirect(url_for("start_quiz"))
    return render_template("login.html")
