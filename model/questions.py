import csv
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
    global DATA_PATH
    global DATA_HEADERS
    with open(DATA_PATH) as questions_csv:
        answer_lines = csv.reader(questions_csv, delimiter=',', quotechar='"')
        isfirstline = True
        for answer_line in answer_lines:
            if isfirstline:
                isfirstline = False
                continue
            answer_data = {}
            for column_index in range(len(DATA_HEADERS)):
                answer_data[DATA_HEADERS[column_index]] = answer_line[column_index]
            questions[int(answer_line[0])] = answer_data

    print(questions)
    return questions


def save_questions():
    global questions
    global DATA_PATH
    global DATA_HEADERS

    with open(DATA_PATH, mode='w') as csv_questions:
        writer = csv.DictWriter(csv_questions, fieldnames=DATA_HEADERS)
        writer.writeheader(DATA_HEADERS)
        for data in questions:
            writer.writerow(data)
    load_questions()

    return questions


def get_questions():
    global questions
    return questions


def get_question(question_id):
    global questions
    return questions[question_id]


def add_question(question_data):
    global questions

    new_answer_id = get_id()
    questions[new_answer_id] = question_data
    save_questions()

    return questions


def edit_question(question_id, question_data):
    global questions

    questions[question_id] = question_data
    save_questions()

    return questions


def get_id():
    global questions
    id_list = questions.keys()

    return int(max(id_list))+1
