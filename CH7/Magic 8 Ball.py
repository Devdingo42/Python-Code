# File: <Magic 8 Ball>
# Description: <Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
# random response to a yes or no question. In the student sample programs for this book, you
# will find a text file named 8_ball_responses.txt. The file contains 12 responses, such
# as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should
# read the responses from the file into a list. It should prompt the user to ask a question, then
# display one of the responses, randomly selected from the list. The program should repeat
# until the user is ready to quit.>
# Assignment Name and Number: Magic 8 Ball , #7.13
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random

def main():
    ball_responses = ['Yes, of course!', 'Without a doubt, yes.', 'You can count on it.', 'For sure!', 'Ask me later.', "I'm not sure", "I can't tell you right now.",
                 "I'll tell you after my nap.", 'No way!', "I don't think so.", 'Without a doubt, no', 'The answer is clearly NO.']
    outfile = open('8_ball_responses_list.txt', 'w')

    for item in ball_responses:
        outfile.write(item + '\n')
    
    outfile.close()
main()

def main():
   print()
   again = 'y'
   while again == 'y':
    question = input('Please ask the 8 ball a question: ')
    infile = open('8_ball_responses_list.txt', 'r')
    ball_responses = infile.readlines()
    infile.close()
    index = 0
    while index < len(ball_responses):
      ball_responses[index] = (ball_responses[index].rstrip('\n'))
      index += 1
    t = list(ball_responses)
    p = random.choice(t)
    print(p)
    print('Do you want to ask another question')
    again = input('y = yes, anything else = no: ')
    print()
main()