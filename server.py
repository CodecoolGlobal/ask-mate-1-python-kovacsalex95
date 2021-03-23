from flask import Flask
import model.questions as questions
import model.answers as answers

app = Flask(__name__)


@app.route("/")
def main_page():

    questions.load_questions()
    answers.load_answers()

    return "Hello World!"


# /question/<question_id>
@app.route("/question/<question_id>")
def view_question(question_id):
    return 'kekv'


# [GET] /vote ?question_id=[ID] &vote=1
# [POST] /reply question_id=[ID] answer_data={}
# ...


if __name__ == "__main__":
    app.run()
