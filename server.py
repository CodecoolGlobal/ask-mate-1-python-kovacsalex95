from flask import Flask, render_template, redirect, url_for
import model.questions as questions
import model.answers as answers

app = Flask(__name__)


@app.route("/")
def main_page():

    questions.load_questions()
    answers.load_answers()

    all_questions = questions.get_questions()

    return "Hello World!"


@app.route("/question/<question_id>")
def view_question(question_id):

    questions.load_questions()
    answers.load_answers()

    question_data = questions.get_question(question_id)
    question_answers = answers.get_question_answers(question_id)

    return render_template("question.html", question=question_data, answers=question_answers)


# [GET] /vote ?question_id=[ID] &vote=1
# [POST] /reply question_id=[ID] answer_data={}
# ...


if __name__ == "__main__":
    app.run()
