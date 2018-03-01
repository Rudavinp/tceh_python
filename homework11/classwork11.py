from flask import Flask, request, session
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
import os
import random
import config


class CantactForm(FlaskForm):
    number = IntegerField(label='number')
    username = StringField(label='username')

app = Flask(__name__)
app.config.from_object(config)
seed = os.environ['FLASK_RANDOM_SEED']
random.seed(seed)


class RandomNumber(object):
    """
    Класс RandomNumber загадывает случайное число
    метод класса change меняет число на другое
    """
    numb = random.randint(1, 11)

    @classmethod
    def change(cls):
        cls.numb = random.randint(1, 11)


@app.route('/', methods=['GET', ])
def home():
    if 'username' not in session:
        return 'U not login. Please login on "http://127.0.0.1:5000/login"'
    return 'Число загаданно'


@app.route('/login', methods=['POST', ])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['numbers_trying'] = 0
        session['numbers_guess'] = 0
    return 'U login'


@app.route('/quess', methods=['POST', ])
def guess():
    if 'username' not in session:
        return 'U not login. Please login on "http://127.0.0.1:5000/login"'
    if request.method == 'POST':
        session['numbers_trying'] += 1
        guess_number = RandomNumber.numb
        user_number = int(request.form['number'])
        
        if user_number > guess_number:
            answer = '>'
        elif user_number < guess_number:
            answer = '<'
        else:
            answer = '='
            RandomNumber.change()
            session['numbers_guess'] += 1
        return answer


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('numbers_trying', None)
    session.pop('numbers_guess', None)
    return 'U logout'

if __name__ == '__main__':
    app.run()