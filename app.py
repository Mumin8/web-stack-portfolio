from quiz import app
from quiz.routes import index
from quiz.routes import user_route, Quiz

'''app'''


if __name__=="__main__":
    '''Entry point'''
    app.run(debug=True)