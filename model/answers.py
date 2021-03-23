
import csv

answers = {}
DATA_PATH = 'data/answer.csv'
DATA_HEADERS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

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
    global DATA_PATH
    global DATA_HEADERS
    with open(DATA_PATH) as answers_csv:
        answer_lines = csv.reader(answers_csv, delimiter=',', quotechar='"')
        isfirstline = True
        for answer_line in answer_lines:
            if isfirstline:
                isfirstline = False
                continue
            answer_data = {}
            for column_index in range(len(DATA_HEADERS)):
                answer_data[DATA_HEADERS[column_index]] = answer_line[column_index]
            answers[int(answer_line[0])] = answer_data

    print(answers)
    return answers


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
    return answers[answer_id]


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


load_answers()
