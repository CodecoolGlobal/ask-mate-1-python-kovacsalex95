
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
    global answers
    global DATA_PATH
    global DATA_HEADERS
    with open(DATA_PATH, mode='w') as csv_answers:
        writer = csv.DictWriter(csv_answers, fieldnames=DATA_HEADERS)
        writer.writeheader(DATA_HEADERS)
        for data in answers:
            writer.writerow(data)
    load_answers()


def get_question_answers(question_id):
    global answers
    question_answers = {}

    for answer in range(len(answers)):
        if answers[answer]['question_id'] == question_id:
            question_answers[id] = answers[answer]

    return question_answers


def get_answer(answer_id):
    global answers
    return answers[answer_id]


def add_answer(question_id, answer_data):
    global answers

    # add new answer
    new_answer_id = get_id()
    answers[new_answer_id] = answer_data
    save_answers()

    return answers


def edit_answer(answer_id, answer_data):
    global answers

    # edit answers[id] ...
    answers[answer_id] = answer_data

    save_answers()
    return answers


def vote_answer(answer_id, vote):
    # vote can be +1/-1
    global answers
    answers[answer_id]['vote_number'] += vote
    save_answers()

    return answers


def get_id():
    global answers
    id_list = answers.keys()

    return int(max(id_list))+1


