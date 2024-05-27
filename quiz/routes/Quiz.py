from quiz import app, db
from flask import render_template, url_for, redirect, request, jsonify
from flask_login import current_user
from quiz.models.User import Quiz


@app.route("/start_quiz")
def start_quiz():
    '''
    the quiz will start from when if and only if the user is authenticated
    '''
    
    if current_user.is_authenticated:
        prev = Quiz.query.filter_by(id=current_user.id).first()
        questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Rome"],
                "answer": "Paris" 
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"  
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Mount Kilimanjaro", "Denali"],
                "answer": "Mount Everest"  
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Cellular respiration", "Meiosis", "Mitosis", "Photosynthesis"],
                "answer": "Photosynthesis"  
            }
        ]
        
        return render_template('quiz.html', questions=questions, prev = prev.result)
    return redirect(url_for('login'))


@app.route("/save_result", methods=['GET', 'POST'])
def save_result():
    '''
    the result will be saved from here 
    '''

    result = request.form['key']
    quiz = Quiz.query.filter_by(id=current_user.id).first()
    if quiz:
        quiz.update(result)
    else:
        quiz_result = Quiz(result=result)
        db.session.add(quiz_result)
        db.session.commit()
    return jsonify(result='success', data_processed='something here')