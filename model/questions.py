DATA_PATH = 'data/question.csv'
DATA_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

questions = {}
'''

{
    [QUESTION_ID]: {
        vote_number: 3
        submission_time: ...
        ...
    }
}

'''

def load_questions():
    global questions
    pass


def save_questions(questions_data):
    # save

    # load_questions()
    pass


def get_questions():
    global questions
    return questions


def get_questions(question_id):
    global questions

    # return questions[id]

    pass


def add_question(question_data):
    global questions

    # add new question

    # save_questions(...)

    # load_questions()

    pass


def edit_question(question_id, question_data):
    global questions

    # edit questions[id] ...

    # save_questions(...)

    # load_questions()

    pass
