#!/usr/bin/python3
import json
import time

TOPIC = ['PerfilDeRiesgo']

def ask_one_question(question):
    print("\n" + question)
    choice = input("Ingresa las alternativas")
    while(True):
        if choice.lower() in ['a']:
            return choice
        else:
            print("Eleccion invalida")
            choice = input("Ingresa eleccion [a]: ")


def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["answer"].lower() == actual.lower():
        print("Q. {0} Absolutamente Correcto!\n".format(key))
        return 2
    else:
        print("Q. {0} Incorrecto!\n".format(key))
        print("Respuesta correcta {0}".format(actual))
        print("Aprender mas: " + meta["more_info"] + "\n")
        return -1

def test(questions):
    score = 0
    print("Test question: ")
    time.sleep(10)
    for key, meta in questions.items():
        questions[key]["answer"] = ask_one_question(meta["question"])
    print("Score: ")
    for key, meta in questions.items():
        score += score_one_result(key, meta["answer"])
    print("Score: ", score, "/", (2*len(questions)))


def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)

def question():
    flag = False
    try:
        choice =int(input('Hola al canal ingresa al perfil de riesgo: (1)\n Ingresa:'))
        if choice  > len(TOPIC) or choice < 1:
            print('Eleccion invalida.')
            flag = True
    except ValueError as e:
        print('Eleccion invalida.')
        flag = True

    if not flag:
        questions = load_question(TOPIC[choice-1]+'.json')
        test(questions)
    else:
        question()


def user_begin():
    print("Hola Este es una prueba")
    play = input()
    if play.lower() == 'a' or play.lower() == 'y':
        question()
    elif play.lower() == 'b':
        print("Gracias por todo")
    else:
        print("Hmm... No entendi asi que repetire")
        user_begin()

def execute():
    user_begin()

if __name__ == "__main__":
    execute()