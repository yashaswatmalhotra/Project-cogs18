"""A collection of function for doing my project."""

import json

def database(test_mode = False):
    
    """Starts the database interface and gives the user the choice to view the different datasets present in the database
    
    Parameters
    ----------
    Input 1: test_mode, bool, Optional - Primarily used for testing
    If false, the user will be shown the database interface.
    If true, test_mode is active and the database  interface will not show up.
    
    Returns
    -------
    output: Based on the test_mode
    Returns one of three data dictionaries based on the user's input if test_mode is False
    Returns a string for testing purposes if the test_mode is True
           
    """
    
    #This function works when test_mode is False
    #Uses the user's input choice to return user's demanded dataset
    
    
    if test_mode == False:
        
        name = input("Please enter your name: ")
        print('Hi, '+ name, '\nWelcome to the coronavirus USA Data base. Curruntly, The United States has the highest number of coronavirus    cases!')
    
        #While loop acts as a switch that allows user to look at all different statistics before exiting the database
        #While chat is True, the databse will be open
        chat =True
        while chat:
            options = input('Please select what exactly you would like to know\nType a for weekly analysis of new cases\nType'
                      ' b for weekly analysis of deaths\nType' 
                      ' c for data about cases per age group\nType'
                      ' d to look at some important global stats\n\nType'
                      ' end to exit the database')
        
            if options == 'a':
                output = weekly_cases
        
            elif options == 'b':
                output = weekly_death
        
            elif options == 'c':
                output = cases_age_group
        
            elif options == 'd':
                output = imp_stats

            elif options == 'end':
                output = 'Hope you learnt something today!'
                chat = False
                
            else:
                output = 'Oops, seems like you entered the wrong input. Please try again!'
            
            print(json.dumps(output, indent = 0), options)
    
    if test_mode == True:
        
        output = 'This is a test mode'
        
        return output
    
weekly_cases = {
            'week 1':5,
            'week 2':6,
            'week 3':1,
            'week 4':1,
            'week 5':2,
            'week 6':63,
            'week 7':859,
            'week 8':6086,
            'week 9':47430,
            'week 10':131648,
            'week 11':209825,
            'week 12':209464,
            'week 13':197193,
            'week 14':202564,
            'week 15':188666,
            'week 16':170248,
            'week 17':164174,
            'week 19':147428,
            'week 20':143578
             }

weekly_death = {'week 1':0,
            'week 2':1,
            'week 3':0,
            'week 4':3,
            'week 5':5,
            'week 6':32,
            'week 7':52,
            'week 8':545,
            'week 9':3018,
            'week 10':9412,
            'week 11':15505,
            'week 12':16042,
            'week 13':13685,
            'week 14':10969,
            'week 15':9779,
            'week 16':7322,
            'week 17':4025,
            'week 19':1163,
            }

cases_age_group = {
    '0-17':64177,
    '18-44':610237,
    '45-64':514963,
    '65-74':150837,
    '75+': 178630,
}

imp_stats = {
    'Total cases': 7316690,
    'Total deaths': 412997,
    'Active cases': 3303688,
    'Percent of active cases in critical condition': 2,
    'Total recovered': 3594975,
    'Closed cases': 4007972,
    'Percent death in closed cases': 10
}


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


def begin(test_mode = False, input_choice = 'default'):
    
    """ Begins the program and gives user the option of choosing between giving a quiz or looking at the database
    
    Parameters
    ----------
    Input 1, test_mode: bool, Optional 
    If false, the user will be given an option between giving a quiz or viewing a program.
    If true, test_mode is active and the choice based interface will not show up
    
    Input 2, input_choice:, str, Optional
    input_choice is primarily used for testing when test_mode is True 
    No inputs required to run the function. Two default inputs are present that need not be changed to run the function. 
    
    Returns
    -------
    output: Based on the test_mode
    Returns either a fuction for a quiz or a database interface if test_mode is False
    Returns input_choice for testing purposes if test_mode is True
    """
    
    #Checks if test_mode is inactive to provide an option for selecting a quiz or a databse
    if (test_mode == False):
        choice = input('Welcome to the Coronavirus interface! What would you like to do first\n'
                   'Press a to play a quiz to test your knowledge about the coronavirus'
                   ' or,\nPress b to look at the country database: ')
        
    elif (test_mode == True):
        choice = input_choice

    #Uses user's input option to present either a quiz or a database if test_mode is false
    #This portion is also used for testing purposes if test_mode is True
    if choice == 'a':
        if test_mode:
            return 'a'
        output = perform_quiz(False, question_answers)
        
        return output
        
    elif choice == 'b':
        if test_mode:
            return 'b'
        output = database()
        
        return output
    
    