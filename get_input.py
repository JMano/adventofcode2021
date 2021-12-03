import requests, os.path
import datetime

def get_day(day):
    return '0' + day if int(day) < 10 else day

def get_input_for_day(session, day):
    day_for_folder = get_day(day)
    year = str(datetime.date.today().year)

    with open('.session') as session_file:
        session = session_file.read()

    directory = 'Day' + day_for_folder
    input_file_path = directory + '/input.txt'

    if not os.path.exists(input_file_path):
        if not os.path.exists(directory):
            os.makedirs(directory)

        cookies = {
            'session': session,
        }

        response = requests.get('https://adventofcode.com/' + year + '/day/'+ day + '/input', cookies=cookies)

        with open(input_file_path, 'w') as input_file:
            content = response.content.decode()
            input_file.write(content)

            return content.split('\n')
    else:
        with open(input_file_path) as input_file:
            return input_file.read().split('\n')

def get_test_input_for_day(day):
    day_for_folder = get_day(day)
    
    directory = 'Day' + day_for_folder
    input_file_path = directory + '/test_input.txt'

    with open(input_file_path) as input_file:
        return input_file.read().split('\n')