from flask import Flask, render_template, redirect, request
import model.questions as questions
import model.answers as answers

app = Flask(__name__)


@app.route("/")
def main_page():
    home_data = homepage_data()

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
        new_question = {}

        title = request.values["question-title"]
        message = request.values["question-message"]
        new_question["title"] = title
        new_question["message"] = message
        # todo: image

        questions.add_question(new_question)

    return redirect("/")


@app.route("/question/<question_id>/edit", methods=["POST"])
def edit_question(question_id):
    if request.method == "POST":
        question_data = {}
        title = request.values["question-title"]
        message = request.values["question-message"]
        question_data["title"] = title
        question_data["message"] = message

        questions.edit_question(question_id, question_data)

    return question_url(question_id)


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

    return question_url(question_id)


# ANSWERS


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def answer_question(question_id):
    if request.method == "POST":
        answer_data = {}

        message = request.values["answer-message"]
        answer_data['message'] = message
        # todo: image

        answers.add_answer(question_id, answer_data)

    return question_url(question_id)


@app.route('/answer/<answer_id>/edit-answer', methods=['POST'])
def edit_answer(answer_id):
    if request.method == 'POST':
        answer_data = {}

        message = request.values["answer-message"]
        answer_data['message'] = message
        # todo: image

        answers.edit_answer(answer_id, answer_data)

        answer_data = answers.get_answer(answer_id)
        question_id = answer_data['question_id']

        return question_url(question_id)

    return redirect('/')


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    answer_data = answers.get_answer(answer_id)
    question_id = answer_data['question_id']

    answers.delete_answer(answer_id)

    return question_url(question_id)


@app.route("/vote-answer/<answer_id>", methods=["GET"])
def answer_vote(answer_id):
    if request.method == "GET":
        answer_data = answers.get_answer(answer_id)
        question_id = answer_data['question_id']

        vote = request.args["vote"]
        answers.vote_answer(answer_id, vote)

        return question_url(question_id)

    return redirect('/')


# MISC

def homepage_data():
    print(answers.get_answers())

    all_question = questions.get_questions()

    results = {}

    for question_id in all_question.keys():
        question_data = all_question[int(question_id)].copy()
        question_data['answers'] = answers.get_question_answers(int(question_id))
        question_data['answers_class'] = 'hidden' if len(question_data['answers']) == 0 else ''

        results[int(question_id)] = question_data

    return results


def question_url(question_id):
    return redirect("/question/" + str(question_id))


if __name__ == "__main__":
    questions.load_questions()
    answers.load_answers()

    app.run()
