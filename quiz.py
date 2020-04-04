class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "\n1. Is Mount Shasta an active volcano?\n(a) Yes\n(b) No\n(c) I hope not!\n\n",
     "\n2. On average how often does Mount Shasta erupt?\n(a) Never\n(b) Every 60 years\n(c) Every 600 years\n\n",
     "\n3. How long have people lived near Mount Shasta?\n(a) 700 years\n(b) 7,000 years\n(c) 70,000 years\n\n",
     "\n5. What is the elevation of Mount Shasta?\n(a) 14,179 feet\n(b) 14,179 meters\n(c) 14,179 miles\n\n",
     "\n5. What is the estimated volume of Mount Shasta?\n(a) 5 cubic miles\n(b) 85 cubic miles\n(c) 350 cubic kilometers\n\n",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
]

def run_test(questions):
     print("\n")
     print("Welcome to my 2020 Hackathon Mini Quiz\n")
     score = 0
     for question in questions:
          answer = raw_input(question.prompt)
          if answer == question.answer:
               score += 1
     print("\n")
     print("You got " + str(score) + "/" +str(len(questions)) +" correct")
     print("\n")


run_test(questions)
