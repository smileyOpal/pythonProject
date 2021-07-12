import codecs
import csv
import os.path
import math
import constants


def read_csv_file(file_path, headers=[], has_header=True):
    print('============READ FILE - {0}============'.format(file_path))
    csv_file = codecs.open(file_path, 'r', 'utf-8-sig')
    reader = csv.DictReader(csv_file, headers)
    if has_header:
        return list(reader)[1:]
    else:
        return list(reader)


def create_directory(subdirectory):
    try:
        os.mkdir(subdirectory)
    except Exception:
        pass


def get_dict_header(dict_data):
    if len(dict_data) > 0:
        header = dict_data[0].keys()
        for data in dict_data:
            keys = data.keys()
            if len(keys) > len(header):
                header = keys
        return header
    else:
        return []


def write_result_to_file(dict_data, csv_file_name, subdirectory='result', headers=[], mode='w'):
    print('===========WRITE_FILE===============')
    print('total records: ' + str(len(dict_data)))
    try:
        create_directory(subdirectory)
        file_path = os.path.join(subdirectory, csv_file_name)
        csv_file = codecs.open(file_path, mode, 'utf-8-sig')
        if len(headers) is 0:
            headers = get_dict_header(dict_data)
        wr = csv.DictWriter(csv_file, headers)
        wr.writeheader()
        for data in dict_data:
            wr.writerow(data)
        csv_file.close()

    except IOError as errno:
        print("I/O error({0})".format(errno))
    print('success')
    return


def split_files(file_path):
    read_file = read_csv_file(file_path)
    data_length = len(read_file)
    no_files = int(math.ceil(float(data_length) / constants.default_file_size)) + 1

    start = 0
    for i in range(1, no_files):
        end = constants.default_file_size * i
        write_result_to_file(read_file[start:end], 'result_{0}.csv'.format(i), 'result', get_dict_header(read_file))
        start = end


if __name__ == '__main__':
    read = read_csv_file('sample.csv')
    print read
    split_files('sample.csv')