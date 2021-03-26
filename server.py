from flask import Flask, render_template, redirect, request
import model.questions as questions
import model.answers as answers
import util
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def main_page():
    home_data = util.homepage_data()

    return render_template("/main.html", data=home_data)


# QUESTIONS


@app.route("/question/<question_id>")
def view_question(question_id):

    question_data = questions.get_question(question_id)
    question_answers = answers.get_question_answers(question_id)

    return render_template("question.html", question=question_data, answers=question_answers)


@app.route("/add-question", methods=["POST"])
def add_question():
    if request.method == "POST":
        # edit mode
        if request.values['form-type'] == 'edit' and request.values['edit-id'].isnumeric() and int(request.values['edit-id']) >= 0:
            return edit_question(int(request.values['edit-id']), request.values)

        filename = ''

        if 'question-image' in request.files:
            file = request.files['question-image']
            if file.filename != '' and file and util.allowed_file(file.filename, ALLOWED_EXTENSIONS):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_question = {}

        title = request.values["question-title"]
        message = request.values["question-message"]
        new_question["title"] = title
        new_question["message"] = message
        new_question["image"] = '' if filename == '' else UPLOAD_FOLDER + '/' + filename

        questions.add_question(new_question)

    return redirect("/")


# kommenteltem mivel ez a hozzáadó formból fog működni kekw
# @app.route("/question/<question_id>/edit", methods=["POST"])
def edit_question(question_id, request_values):
    question_data = {}
    title = request_values["question-title"]
    message = request_values["question-message"]
    question_data["title"] = title
    question_data["message"] = message

    questions.edit_question(question_id, question_data)

    return util.question_url(question_id)


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    questions.delete_question(question_id)
    answers.delete_question_answers(question_id)

    return redirect("/")


@app.route("/vote-question/<question_id>", methods=["GET"])
def question_vote(question_id):
    if request.method == "GET":
        vote = request.args["vote"]
        questions.vote_question(question_id, vote)

    return util.question_url(question_id)


# ANSWERS


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def answer_question(question_id):
    if request.method == "POST":
        # edit mode
        if request.values['form-type'] == 'edit' and request.values['edit-id'].isnumeric() and int(request.values['edit-id']) >= 0:
            return edit_answer(int(request.values['edit-id']), request.values)

        answer_data = {}

        message = request.values["answer-message"]
        answer_data['message'] = message
        # todo: image

        answers.add_answer(question_id, answer_data)

    return util.question_url(question_id)


#kommenteltem mivel ez a hozzáadó formból fog működni kekw
# @app.route('/answer/<answer_id>/edit-answer', methods=['POST'])
def edit_answer(answer_id, request_values):
    answer_data = {}

    message = request_values["answer-message"]
    answer_data['message'] = message
    # todo: image

    answers.edit_answer(answer_id, answer_data)

    answer_data = answers.get_answer(answer_id)
    question_id = answer_data['question_id']

    return util.question_url(question_id)


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    answer_data = answers.get_answer(answer_id)
    question_id = answer_data['question_id']

    answers.delete_answer(answer_id)

    return util.question_url(question_id)


@app.route("/vote-answer/<answer_id>", methods=["GET"])
def answer_vote(answer_id):
    if request.method == "GET":
        answer_data = answers.get_answer(answer_id)
        question_id = answer_data['question_id']

        vote = request.args["vote"]
        answers.vote_answer(answer_id, vote)

        return util.question_url(question_id)

    return redirect('/')


if __name__ == "__main__":
    questions.load_questions()
    answers.load_answers()

    app.run()
