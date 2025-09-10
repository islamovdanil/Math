from flask import Flask, render_template, request, session, redirect, url_for
import random
from decouple import config

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')


def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b, a * b


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'attempts' not in session:
        session['attempts'] = 3
        session['question'], session['second_number'], session['answer'] = generate_question()

    if request.method == 'POST':
        user_answer = request.form.get('answer')

        if user_answer is None:
            return redirect(url_for('index'))

        try:
            user_answer = int(user_answer)
        except ValueError:
            return render_template('index.html',
                                   message="Пожалуйста, введите число!",
                                   question=session['question'],
                                   second_number=session['second_number'],
                                   attempts=session['attempts'])

        # Добавляем проверку диапазона
        if user_answer < 1 or user_answer > 100:
            return render_template('index.html',
                                   message="Ошибка! Ответ должен быть от 1 до 100",
                                   question=session['question'],
                                   second_number=session['second_number'],
                                   attempts=session['attempts'])

        if user_answer == session['answer']:
            session.pop('attempts', None)
            session.pop('question', None)
            session.pop('second_number', None)
            session.pop('answer', None)
            return render_template('index.html',
                                   message="Правильно! Ты молодец!",
                                   new_game=True)
        else:
            session['attempts'] -= 1
            if session['attempts'] == 0:
                session.pop('attempts', None)
                session.pop('question', None)
                session.pop('second_number', None)
                session.pop('answer', None)
                return render_template('index.html',
                                       message="Увы, попытки закончились! Попробуй снова.",
                                       new_game=True)
            return render_template('index.html',
                                   message="Неправильно, попробуй еще раз!",
                                   question=session['question'],
                                   second_number=session['second_number'],
                                   attempts=session['attempts'])

    return render_template('index.html',
                           question=session['question'],
                           second_number=session['second_number'],
                           attempts=session['attempts'])


if __name__ == '__main__':
    app.run(debug=True)
