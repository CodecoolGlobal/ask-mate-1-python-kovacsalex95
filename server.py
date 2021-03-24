from flask import Flask, render_template, redirect, url_for, request
import model.questions as questions
import model.answers as answers

app = Flask(__name__)


@app.route("/")
def main_page():

    questions.load_questions()
    answers.load_answers()

    all_questions = questions.get_questions()

    return render_template("/main.html", all_questions=all_questions)


@app.route("/question/<question_id>")
def view_question(question_id):

    questions.load_questions()
    answers.load_answers()

    question_data = questions.get_question(question_id)
    question_answers = answers.get_question_answers(question_id)

    return render_template("question.html", question=question_data, answers=question_answers)


@app.route("/list")
def question_list():
    questions.load_questions()
    answers.load_answers()
    list_questions = questions.get_questions()
    return render_template("question.html", questions=list_questions)
# [GET] /vote ?question_id=[ID] &vote=1
# [POST] /reply question_id=[ID] answer_data={}
# ...


@app.route("/add-question", methods="POST")
def add_question():
    add_question = {}
    if request.methods == "POST":
        title = request.values["question-title"]
        message = request.values["question-message"]
        add_question["title"] = title
        add_question["message"] = message
        questions.add_question(add_question)
    return redirect("/")


@app.route("/question/<question_id>/new-answer", methods="POST")
def post_answer(question_id, answer_data):
    questions.load_questions()
    answers.load_answers()
    if request.methods == "POST":
        question_data = questions.get_question(question_id)
        new_answer = answers.add_answer(question_id, answer_data)
    return redirect("/question")


@app.route("/question/<question_id>/delete")
def delete_questions(question_id):
    questions.load_questions()
    questions.delete_question(question_id)
    return redirect("/question")


@app.route("/question/<question_id>/edit", methods="POST")
def edit_question(question_id):
    question_data = {}

    if request.methods=="POST":
        title = request.values["question-title"]
        message = request.values["question-message"]
        question_data["title"] = title
        question_data["message"] = message
        questions.edit_question(question_id, question_data)

    return redirect("/question")


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    answers.load_answer()
    answers.delete_answer(answer_id)
    return redirect("/answer")


@app.route("/vote/<question_id>", methods=["GET"])
def question_vote(question_id):
    if request.method=="GET":
        vote = request.args["vote"]
        questions.vote(question_id, vote)
    return redirect("/question/"+str(question_id))


@app.route("/vote/<answer_id>", methods=["GET"])
def question_vote(answer_id):
    if request.method=="GET":
        vote = request.args["vote"]
        questions.vote(answer_id, vote)
    return redirect("/question/"+str(answer_id))


if __name__ == "__main__":
    app.run()
