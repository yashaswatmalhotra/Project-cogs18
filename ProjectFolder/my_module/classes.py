"""Classes used throughout project"""
class Quiz:
    
    """
    This is a class for the Quiz's questions and answers
    
    Attributes:
    ----------
    ask(str): The questions that are to be asked
    answer(str): The correct option to the question
    correct(str): The message displayed if the correctt answer is chosen
    wrong(str): The message displayed if the incorrect answer is chosen
    """
    
    def __init__(self, ask, answer, correct, wrong):
        self.ask = ask
        self.answer = answer
        self.correct = correct
        self.wrong = wrong
        

questions_to_ask = [
    '1) How long can coronavirus stay on surfaces?\n(a) A few hours\t(b) About 30 minutes\t(c) One day\t(d) Two to Three Days',
    '2) Can you get the coronavirus from just touching a dirty surface?\n(a) Yes\t(b)No',
    '3) How long is the incubation period of the Virus?\n(a) One day\t(b) One week\t(c) Up to 14 days',
    '4) What are the areas through which the coronavirus can enterr the body?\n(a) The mouth\t(b) The nose\t(c) The eyes\t(d) All of these',
    '5) Acoording to the social distancing protocol, how much distance must you maintain?\n(a)6 feet\t(b) 0 feet, lets hug\t(c) 2 feet',
    '6) Which of the follwong is not a symotom of the coronavirus?\n(a) Sneezing\t(b) Vomiting\t(c) Loss of taste or smell\t(d) Fever',
    '7) How long should you be washing your hands for?\n(a) 10 seconds\t(b) 1 minutes\t(c) 20 seconds\t(d) 5 seconds',
    '8) Is there currently a cure for the coronavirus?\n(a) Yes\t(b) No',
    '9) What is the genetic makeup of the coronavirus?\n(a) DNA\t(b) RNA\t(c)Protein',
    '10) Is it possible for the coronavirus to mutate and change?\n(a) Yes\t(b) No'
]

#Inherits from the class Quiz and contains the questions, the answers and the messages that will be displayed
question_answers= [
     Quiz(questions_to_ask[0], 'd', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (d)'),
     Quiz(questions_to_ask[1], 'b', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (b)'),
     Quiz(questions_to_ask[2], 'c', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (c)'),
     Quiz(questions_to_ask[3], 'd', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (d)'),
     Quiz(questions_to_ask[4], 'a', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (a)'),
     Quiz(questions_to_ask[5], 'a', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (a)'),
     Quiz(questions_to_ask[6], 'c', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (c)'),
     Quiz(questions_to_ask[7], 'b', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (b)'),
     Quiz(questions_to_ask[8], 'b', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (b)'),
     Quiz(questions_to_ask[9], 'a', '\nCongratulations, thats correct !','\nThat is incorrect! The correct answer was (a)')     
]

Score = 0
Output = ''


def perform_quiz(test_mode = False, questions = 'default'):
    """Begin's the quiz feature of the program. Checks to see  if the answers provided were correct and 
       gives a message at the end based on the score
       
       Parameters
       ----------
       Input 1: test_mode, bool, Optional - Primarily used for testing
       If false, the user will be given a quiz.
       If true, test_mode is active and the quiz interface will not show up.
    
       Input 2: questions, list
       Should contain a list of items that inherit from the Quiz class
       
       Returns
       -------
       1: Score, int
       Users correct points out of 10.
       
       2: Output, str
       Message provided based on user's score
       
    
    """
    # Checks to see if test mode is active and runs the quiz interface if test_mode is false by providing an input choice
    
    if test_mode == True:
        return 'This is the test mode'
        
    elif test_mode == False:
        name = input("Please enter your name: ")
        print('Welcome to the quiz', name,'\nThis quiz is designed to test your knowledge about the virus\nand' 
              ' see how intellectually prepared you are for the VIRUS!\n \n'
              'GOOD LUCK')
        score = 0
        
        # Checks if the user's input choice matches with the corrct answer that is also provided in the list
        # Informs user if their answer is correct or incorrect 
        # Adds 1 to the score if user's input matches the correct choice
        for question in question_answers:
                answer = input(question.ask+'\nYour answer - ')
                if answer == question.answer:
                    score += 1
                    print(question.correct)
                elif answer != question.answer:
                    print(question.wrong)
        
        print('\nYour score was', score, 'out of 10')
        
        if score <=3:
            output = 'Your score was very low! Make sure you learn more about the coronavirus to make sure you stay safe!'
        
        elif score >= 4 and score < 7:  
            output = 'Your score was decent. Make sure you keep learning to be prepared'
        
        elif score == 10:
            output = 'CONGRATULATIONS! You had a perfect score. Make sure to spread the knowledge'
        
        else: 
            output = 'Your score was very good! You seem intelectually ready! Good job'
        
        Score = score
        Output = output
        
        return Output

        

possible_score = ['Your score was very low! Make sure you learn more about the coronavirus to make sure you stay safe!',
                  'Your score was very low! Make sure you learn more about the coronavirus to make sure you stay safe!',
                  'Your score was very low! Make sure you learn more about the coronavirus to make sure you stay safe!',
                  'Your score was very low! Make sure you learn more about the coronavirus to make sure you stay safe!',
                  'Your score was decent. Make sure you keep learning to be prepared',
                  'Your score was decent. Make sure you keep learning to be prepared',
                  'Your score was decent. Make sure you keep learning to be prepared',
                  'Your score was very good! You seem intelectually ready! Good job',
                  'Your score was very good! You seem intelectually ready! Good job',
                  'Your score was very good! You seem intelectually ready! Good job',
                  'CONGRATULATIONS! You had a perfect score. Make sure to spread the knowledge'
                 ] 



