from questions import Questions

question_prompts = [
    "What is the capital city of Canada?\n (a) Toronto\n(b) Vancouver\n(c) Ottawa\n(d) Montreal\n\n",
    "Which planet is known as the Red Planet?\n (a) Venus\n(b) Mars\n(c) Jupiter\n(d) Saturn\n\n",
    "Who wrote the play Romeo and Juliet?\n (a) Charles Dickens\n(b) William Shakespeare\n(c) George Orwell\n(d) Jane Austen\n\n",
    "What is the largest ocean on Earth?\n (a) Atlantic Ocean\n(b) Indian Ocean\n(c) Pacific Ocean\n(d) Arctic Ocean\n\n",
    "Which element has the chemical symbol 'O'?\n (a) Gold\n(b) Oxygen\n(c) Osmium\n(d) Ozone\n\n"
]

questions = [
    Questions(question_prompts[0], "c"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "b"),
    Questions(question_prompts[3], "c"),
    Questions(question_prompts[4], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).strip().lower()
        if answer == question.answer.lower():
         score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)