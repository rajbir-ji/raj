# Quiz Game
print("Welcome to the Quiz Game!")
score = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    { 
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
        "answer": "B"
    }
]
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")
print(f"\nYour final score is: {score}/{len(questions)}")
