#millionaire

questions = [
    ["What is the output of print(2 ** 3)?", "5", "6", "8", "9", 3],
    ["Which keyword is used to define a function in Python?", "func", "def", "function", "define", 2],
    ["What data type is the object below?\nL = [1, 23, 'hello', 1]", "List", "Dictionary", "Tuple", "Set", 1],
    ["What is the output of print(len('Hello'))?", "3", "4", "5", "6", 3],
    ["Which of the following is a Python tuple?", "[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "{1: 'a', 2: 'b', 3: 'c'}", 2],
    ["How do you insert COMMENTS in Python code?", "// This is a comment", "# This is a comment", "/* This is a comment */", "<!-- This is a comment -->", 2],
    ["Which method can be used to convert a string to lowercase?", ".lower()", ".uppercase()", ".tolower()", ".downcase()", 1],
    ["What is the correct file extension for Python files?", ".pyth", ".pt", ".py", ".pyt", 3],
    ["How do you create a variable with the numeric value 5?", "x = 5", "x = int(5)", "Both of the above", "None of the above", 3],
    ["Which operator is used for floor division in Python?", "/", "//", "%", "**", 2]
]


price = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
i = 0
count = 0
for question in questions:
    print(question[0])
    print("A:", question[1])
    print("B:", question[2])
    print("C:", question[3])
    print("D:", question[4])
    #answer = int(input("Your answer (1 for A, 2 for B, 3 for C, 4 for D): "))
    answer = input("Choose anyone A/B/C/D: ").strip().upper()

    if ord(answer)-65+1 == question[5]:
        print("Correct!\n")
        count+=1
        print(f"You have won prize money = {price[i]} ")
    else:
        print("Wrong! The correct answer is:", question[question[5]])
        print("better luck next time!")
        break # Print a newline for better readability
    i+=1    


print(i)
if count != 0:
    print(f"you have won total prize money of {price[i-1]} ")

# End of the game
# This is a simple quiz game that tests your knowledge of Python.
# You can add more questions to the 'questions' list to make it more challenging.
# Feel free to modify the questions and answers as you see fit.
# Enjoy learning Python!
# This code is a simple quiz game that tests your knowledge of Python.
# You can add more questions to the 'questions' list to make it more challenging.
# Feel free to modify the questions and answers as you see fit.
# Enjoy learning Python!        


# ord(A) = 65. convert the answer to an integer by subtracting 65
#chr(65) = A. convert the integer to a character by adding 65

