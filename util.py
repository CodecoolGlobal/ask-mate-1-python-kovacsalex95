import csv


def load_csv_data(path, headers):
    result = {}

    with open(path) as questions_csv:
        data_lines = csv.reader(questions_csv, delimiter=',', quotechar='"')
        isfirstline = True

        for data_line in data_lines:
            if isfirstline:
                isfirstline = False
                continue

            try:
                data = {}
                for column_index in range(len(headers)):
                    value = data_line[column_index]
                    if value.isnumeric():
                        value = int(value)
                    data[headers[column_index]] = value

                result[int(data_line[0])] = data
            except IndexError:
                continue

    return result.copy()


def write_csv_data(path, header, csv_data):
    write_lines = [','.join(header)]

    for data_key in csv_data.keys():
        data_row = csv_data[data_key]

        data = []

        for column in header:
            chunk = str(data_row[column])

            chunk = chunk.replace('\n', '<br>').replace('"', "'")

            if ',' in chunk:
                chunk = '"' + chunk + '"'

            data.append(chunk)

        write_lines.append(','.join(data))

    file_write = open(path, 'w')

    for write_line in write_lines:
        file_write.write(write_line + '\n')

    file_write.close()
