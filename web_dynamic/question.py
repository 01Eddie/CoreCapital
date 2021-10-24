#!/usr/bin/python3

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

def run_question(questions):
     score = 0
     for question in questions:
        #for answer in question.answer:
        answer = input(question.prompt)
        if answer == question.answer:
               score += 1
        print("Tienes", score, "de", len(questions), " Preguntas")


question_prompts = [
     ["Preg1?\n(a) 1\n(b) 2\n(c) 3\n"],
     ["Preg2?\n(a) 1\n(b)2\n(c) 3\n"],
     ["Preg3?\n(a) 1\n(b)2\n(c) 3\n"],
     ["Preg4?\n(a) 1\n(b)4\n(c) 3\n"],
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "b"),
]


run_question(questions)
