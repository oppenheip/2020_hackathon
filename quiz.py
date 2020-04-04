class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Is Mount Shasta an active volcano?\n(a) Yes\n(b) No\n(c) I hope not!\n\n",
     "On average how often does Mount Shasta erupt?\n(a) Never\n(b) Every 60 years\n(c) Every 600 years\n\n",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "c"),
]

def run_test(questions):
     print("Welcome to my 2020 Hackathon Mini Quiz\n")
     score = 0
     for question in questions:
          answer = raw_input(question.prompt)
          if answer == question.answer:
               score += 1
     print("You got " + str(score) + "/" +str(len(questions)) +" correct")


run_test(questions)
