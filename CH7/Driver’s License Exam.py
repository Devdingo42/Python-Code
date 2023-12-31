# File: <Driver’s License Exam>
# Description: <Your program should store these correct answers in a list. The program should read the
# student’s answers for each of the 20 questions from a text file and store the answers in
# another list. (Create your own text file to test the application.) After the student’s answers
# have been read from the file, the program should display a message indicating whether the
# student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
# to pass the exam.) It should then display the total number of correctly answered questions,
# the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.>
# Assignment Name and Number: Driver’s License Exam , #7.7
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

Answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
              'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

def main():
   My_Answers = []
   for x in range(20):
      Problem = input('Please enter the correct letter "A", "B", "C","D": ')
      My_Answers.append(Problem)
   outfile = open('My_Answerslist.txt', 'w')

   for item in My_Answers:
     outfile.write(item + '\n')
    
   outfile.close()
main()

def main():
   print()
   infile = open('My_Answerslist.txt', 'r')
   My_Answers = infile.readlines()
   infile.close()
   index = 0
   count_correct = 0
   count_wrong = 0
   while index < len(My_Answers):
      My_Answers[index] = My_Answers[index].rstrip('\n')
      if My_Answers[index] == Answers[index]:
         count_correct += 1
      if My_Answers[index] != Answers[index]:
         count_wrong += 1
      index += 1

   print('These are the student answers: ', My_Answers)
   if count_correct < 15:
      print("You have failed the test, you got", count_correct, "right and you got", count_wrong, "wrong")
   if count_correct >= 15:
      print("You have passed the test, you got", count_correct, "right and you got", count_wrong, "wrong")
   if count_correct == 20:
      print('You have no wrong answers. Good Job')
      print('Good job, we dont even have to go over the ones you got wrong, since you got them all right.')
   print()

main()