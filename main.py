import json
import sys
from os import path, getcwd
from pathlib import Path
from random import shuffle


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    END = "\033[0m"
    YELLOW = "\33[33m"


class Test:
    letter_to_index = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14
    }

    def __init__(self, file_path):
        self.file_path = file_path
        self.questions = self._load_questions()

    def _load_questions(self) -> dict:
        if self.file_path != 'all':
            with open(self.file_path) as f:
                f_str = f.read()
            return json.loads(f_str)

        all_questions_dict = dict()
        current_path = Path(getcwd())
        files = current_path.glob('*.json')
        for f in files:
            with open(f) as f:
                f_str = f.read()
            file_json = json.loads(f_str)
            all_questions_dict = all_questions_dict | file_json
        return all_questions_dict


def print_correct_answers(questions, question, answers):
    print("Correct answers: ")
    for answer in answers:
        if questions[question][answer]:
            print(answer)


def main():
    test_file = input('Input the file name of the test: ')

    test_file = f"{test_file}.json" if '.json' not in test_file and test_file != 'all' else test_file

    if test_file != "all" and not path.exists(test_file):
        print(f"{Colors.RED}File '{test_file}' was not found.{Colors.END}")
        sys.exit(1)

    ti = Test(test_file)
    # Gets the questions from the ti TestInstance variable and shuffles them, then loops through them
    questions = list(ti.questions.keys())
    shuffle(questions)
    for question in questions:
        print(question)
        # Gets the answers as a list and then shuffles them
        answers = list(ti.questions[question].keys())
        total_correct_answers = 0
        user_correct_answers = 0
        user_wrong_answers = 0

        shuffle(answers)
        # Zips through the answers and the letter_to_index keys to be able to assign a letter to the answers.
        for (answer, letter) in zip(answers, ti.letter_to_index.keys()):
            print(f"    {letter}.{answer}")
            if ti.questions[question][answer]:
                total_correct_answers += 1
        input_values = input("Answers: ")

        # Loops through the values inputted by the user, maps it to the answer's index and checks if it is wrong.
        for val in input_values:
            idx = ti.letter_to_index[val]
            if not ti.questions[question][answers[idx]]:
                print(f"{Colors.RED}Wrong answer: {answers[idx]}{Colors.END}")
                user_wrong_answers += 1
            else:
                user_correct_answers += 1

        if user_wrong_answers == 0 and user_correct_answers == total_correct_answers:
            print(f"{Colors.GREEN}Correct!{Colors.END}")
        elif user_correct_answers != total_correct_answers and user_wrong_answers == 0:
            print(
                f"{Colors.YELLOW}All your answers are correct, but there are more correct answers you did not choose. {Colors.END}")
            print_correct_answers(ti.questions, question, answers)
        else:
            print_correct_answers(ti.questions, question, answers)

        print("\n\n\n")


if __name__ == '__main__':
    main()
