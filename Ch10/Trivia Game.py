# File: <Trivia Game>
# Description: <In this programming exercise, you will create a simple trivia game for two players. 
#To create this program, write a Question class to hold the data for a trivia question. 
#The program should have a list or a dictionary containing 10 Question objects, one for
#each trivia question. Make up your own trivia questions on the subject or subjects of your
#choice for the objects.>
# Assignment Name and Number: Trivia Game, #10.9
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

class Question:
    def __init__(self, trivia, answer1, answer2, answer3, answer4):
        self.__trivia = trivia
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
    def set_trivia(self, trivia):
        self.__trivia = trivia
    def set_answer1(self, answer1):
        self.__answer1 = answer1
    def set_answer2(self, answer2):
        self.__answer2 = answer2
    def set_answer3(self, answer3):
        self.__answer3 = answer3
    def set_answer4(self, answer4):
        self.__answer4 = answer4
    def get_trivia(self):
        return self.__trivia
    def get_answer1(self):
        return self.__answer1
    def get_answer2(self):
        return self.__answer2
    def get_answer3(self):
        return self.__answer3
    def get_answer4(self):
        return self.__answer4
def main():
    questions = {'What is the Capital of United States of america?, a) Georgia, b) Hawaii, c) Washing D.C., d) California':'c', 
                 'What year was the first iphone made?, a) 1983, b) 2000, c) 2020, d) 2007':'d', 
                 "What is disney's most popular movie?, a) Frozen II, b) Finding Nemo, c) Moana, d) Toy Story 3":'a', 
                 'Who is the richest person in America?, a) Mark Cuban, b) Elon Musk, c) Jeff Bezos, d) Mark Zuckerberg':'b', 
                 'What country is the most populated?, a) United States, b) India, c) China, d) Indonesia':'b', 
                 'What actor plays Ken in the 2023 blockbuster movie "Barbie?", a) Ryan Gosling, b) Tom Hanks, c) Tom Cruis, d) Ryan Reynolds':'a', 
                 'Before embarking on a solo career, Beyoncé was part of what R&B group?, a) Back Stree Boys, b) Jackson 5, c) Destinys Child, d) Beetles':'c', 
                 'What president was a licensed bartender?, a) George Washington, b) Donald Trump, c) Joe Biden, d) Abraham Lincoln':'d', 
                 'What U.S. state grows coffee beans?, a) California, b) Oregon, c) New York, d) Hawaii':'d', 
                 'Who did the U.S. buy Florida from?, a) Spain, b) United Kingdom, c) Germany, d)Portugal':'a'}
    question = list(questions)
    p1 = 0
    p2 = 0

    for key in question[:5]:
        print()
        print(key)
        answer1 = input('Player 1, Please enter the correct letter: ')
        answer2 = answer1
        answer3 = answer2
        answer4 = answer3
        game = Question(key, answer1, answer2, answer3, answer4)
        print()
        if answer1 == questions[key]:
            print('Correct,', game.get_answer1(), ', is the right choice')
            p1 += 1
        else:
            print('Incorrect,',  game.get_answer2(), ', is the wrong choice')
            p1 += 0
        print('The guestion was,', game.get_trivia())
        print('You have answered', game.get_answer3())

    for key in question[5:]:
        print()
        print(key)
        answer1 = input('Player 2, Please enter the correct letter: ')
        answer2 = answer1
        answer3 = answer2
        answer4 = answer3
        game = Question(key, answer1, answer2, answer3, answer4)
        print()
        if answer1 == questions[key]:
            print('Correct,', game.get_answer4(), ', is the right choice')
            p2 += 1
        else:
            print('Incorrect,',  game.get_answer1(), ', is the wrong choice')
            p2 += 0
        print('The guestion was,', game.get_trivia())
        print('You have answered', game.get_answer2())
    
    print()
    print('Player 1 scored,', p1, 'points')
    print('Player 2 scoered,', p2, 'points')
    if p1 > p2:
        print('Congratulations Player 1, you won the Trivia!!!')
        print('Sorry Player 2, try to get more next time.')
    elif p2 > p1:
        print('Congratulations Player 2, you won the Trivia!!!')
        print('Sorry Player 1, try to get more next time.')
    else:
        print("Wow Player 1 and Player 2 are incredible. You tied!!!. Great Job")

main()