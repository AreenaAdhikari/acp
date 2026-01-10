
print("Welcome to the AI Quiz!")
print("Answer the following 5 questions about Artificial Intelligence.\n")
score = 0
total_question = 5
print("1. What does AI stand for?")
print("a) Automated Intelligence")
print("b) Artificial Intelligence")
print("c) Automated Information")
print("d) Artificial Information")
answer1 = input("Your answer (a/b/c/d): ").lower()
if answer1 == "b":
    print("Correct! ✓\n")
    score += 1
else:
    print("Wrong! The correct answer is b) Artificial Intelligence\n")
print("2. Which of these is NOT a type of AI?")
print("a) Narrow AI")
print("b) General AI")
print("c) Super AI")
print("d) Fast AI")
answer2 = input("Your answer (a/b/c/d): ").lower()
if answer2 == "d":
    print("Correct! ✓\n")
    score += 1
else:
    print("Wrong! The correct answer is d) Fast AI\n")
print("3. What is machine learning?")
print("a) Computers learning to fix themselves")
print("b) AI systems that improve with experience")
print("c) Teaching robots to walk")
print("d) Making computers faster")
answer3 = input("Your answer (a/b/c/d): ").lower()
if answer3 == "b":
    print("Correct! ✓\n")
    score += 1
else:
    print("Wrong! The correct answer is b) AI systems that improve with experience\n")
print("4. Which company created ChatGPT?")
print("a) Google")
print("b) Microsoft")
print("c) OpenAI")
print("d) Facebook")
answer4 = input("Your answer (a/b/c/d): ").lower()
if answer4 == "c":
    print("Correct! ✓\n")
    score += 1
else:
    print("Wrong! The correct answer is c) OpenAI\n")
print("5. What does NLP stand for in AI?")
print("a) Natural Language Processing")
print("b) Neural Learning Process")
print("c) Network Language Protocol")
print("d) Natural Learning Program")
answer5 = input("Your answer (a/b/c/d): ").lower()
if answer5 == "a":
    print("Correct! ✓\n")
    score += 1
else:
    print("Wrong! The correct answer is a) Natural Language Processing\n")
percentage = (score / total_questions) * 100
print("=" * 40)
print("QUIZ RESULTS")
print("=" * 40)
print(f"Your score: {score} out of {total_questions}")
print(f"Percentage: {percentage}%")
if score == 5:
    print("Excellent! ")
elif score >= 3:
    print("Good job!")
else:
    print("Keep learning about AI! ")
print("=" * 40)