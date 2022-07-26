from question import Question

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Green\n(c) Purple\n\n",
    "What color are strawberries?\n(a) Red\n(b) Green\n(c) Purple\n\n",
    "What color are eggplants?\n(a) Red\n(b) Green\n(c) Purple\n\n"
]

questions = [
    Question(question_prompts[0], 'b'),
    Question(question_prompts[1], 'a'),
    Question(question_prompts[2], 'c')
]

def run_test(questions):
    score = 0
    for question in questions:
        guess = input(question.prompt)
        if guess == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)