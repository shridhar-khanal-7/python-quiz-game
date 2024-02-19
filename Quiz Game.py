import random

# Displaying Welcome Message!
print('\nWelcome to the Python Quiz Game. Let\'s start the game!')


def play_quiz():
    Questions_list = [
        ' What is the purpose of the append() method in Python?',
        ' What does the import keyword do in Python?',
        ' Which of the following is an example of a mutable data type in Python?',
        ' what is the purpose of the len() function?',
        ' What does the __init__ method in a Python class do?'
    ]

    Options_list = [
        ['a. To remove an element from a list', 'b. To create a new list',
            'c. To add an element to the end of a list', 'd. To reverse the order of elements in a list'],
        ['a. Imports a module or a package', 'b. Defines a new class',
            'c. Exports a module', 'd. Creates a new function'],
        ['a. Tuple', 'b. String', 'c. List', 'd. Set'],
        ['a. To define a new variable', 'b. To get the length of a list or a string',
            'c. To check if a file exists', 'd. To convert a string to lowercase'],
        ['a. Defines a static method', 'b. Deletes an instance of the class',
            'c. Calls the superclass constructor', 'd. Initializes a new instance of the class']
    ]

    correct_answers = ['c', 'a', 'c', 'b', 'd']

    users_guesses = []
    score = 0
    ques_num = 0

    # Presenting Quiz questions!
    for question in Questions_list:
        print('*Python*****Quiz*****Game*')
        print(f'\nQuestion No: {ques_num+1}')
        print(question)

        for option in Options_list[ques_num]:
            print(option)

        users_guess = input('Please enter A, B, C, or D accordingly: ').lower()
        users_guesses.append(users_guess)

        if users_guess == correct_answers[ques_num]:
            score += 1
            print('⭐Correct Answer!👏')
        else:
            print(f'OOPS!😔 Incorrect Answer! The correct answer is: {correct_answers[ques_num]}')

        ques_num += 1

    # Presenting Total Score
    print('\nQuiz completed! Your final score is:', score)

    # Final Message according to the performance
    if score == len(Questions_list):
        print('Hurray!! Congratulations👏 you answered all the questions correct!')
    elif score >= len(Questions_list)/2:
        print('Keep it up! You did a great job!👏')
    else:
        print('Good Try! Keep Trying!')

    # Asking the user if they want to play again!
    play_again = str(input('Do you want to play again? [Yes/No]: ')).lower()
    if play_again == 'yes':
        play_quiz()
    else:
        print('Thank You for playing! Have a good Day! 🙋‍♂️🙋')


# calling the play quiz function
play_quiz()
