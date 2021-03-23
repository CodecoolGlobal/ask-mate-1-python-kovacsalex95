DATA_PATH = 'data/question.csv'
DATA_HEADERS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

answers = {}
'''

{
    [ANSWER_ID]: {
        question_id: -1,
        vote_number: 3
        submission_time: ...
        ...
    }
}

'''


def load_answers():
    global answers
    pass


def save_answers(question_data):
    # save questions

    # load_questions()
    pass


def get_question_answers(question_id):
    global answers

    # return answers[?]

    pass


def get_answer(answer_id):
    global answers

    # return answers[?]

    pass


def add_answer(question_id, answer_data):
    global answers

    # add new answer

    # save_answers(...)

    # load_answers()

    pass


def edit_answer(answer_id, answer_data):
    global answers

    # edit answers[id] ...

    # save_answers(...)

    # load_answers()

    pass


def vote_answer(answer_id, vote):
    # vote can be +1/-1
    global answers

    # edit answers[id] ...

    # save_answers(...)

    # load_answers()

    pass
