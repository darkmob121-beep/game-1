def run_quiz():
    questions = [
        {
            "prompt": "What does CPU stand for?",
            "options": [
                "A) Central Processing Unit",
                "B) Computer Personal Unit",
                "C) Central Program Utility",
                "D) Core Processing Utility",
            ],
            "answer": "a",
        },
        {
            "prompt": "Which programming language was created by Guido van Rossum in 1991?",
            "options": ["A) JavaScript", "B) Python", "C) C++", "D) Ruby"],
            "answer": "b",
        },
        {
            "prompt": "What is the standard port number for unencrypted HTTP web traffic?",
            "options": ["A) 22", "B) 443", "C) 80", "D) 8080"],
            "answer": "c",
        },
        {
            "prompt": "In Linux, what terminal command is used to list files in a directory?",
            "options": ["A) dir", "B) list", "C) ls", "D) show"],
            "answer": "c",
        },
        {
            "prompt": "What does RAM stand for?",
            "options": [
                "A) Readily Available Memory",
                "B) Random Access Memory",
                "C) Rapid Active Module",
                "D) Remote Access Machine",
            ],
            "answer": "b",
        },
    ]

    score = 0
    print("====================================")
    print("      🧠 TECH TRIVIA QUIZ 🧠        ")
    print("====================================")
    print("Test your computer and coding knowledge!\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['prompt']}")
        for option in q["options"]:
            print(f"  {option}")

        answer = input("\nYour answer (a/b/c/d): ").strip().lower()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer'].upper()}.\n")

    print("====================================")
    print("           QUIZ COMPLETED           ")
    print("====================================")
    print(f"Your Final Score: {score} / {len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.0f}%")


if __name__ == "__main__":
    run_quiz()
