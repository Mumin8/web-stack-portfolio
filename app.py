from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
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
        }
       
    ]
    
    return render_template('index.html', questions=questions)

@app.route("/answer")
def anser():
    return render_template('index.html')