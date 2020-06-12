"""Test for my functions.


"""

from my_module.functions import*
from my_module.classes import*

def test_begin():
    #to check if begin is callable
    assert callable(begin)
    
    #to check if the test_mode gives desired testing output and 
    #to ensure that when test_mode is True, a secondary interface is not opened
    assert begin(True, 'a') == 'a'
    assert begin(True, 'b') == 'b'
    
    
def test_perform_quiz():
    
    #to check if perform_quiz is callable
    assert callable(perform_quiz)
    
    #to check if the test_mode gives desired testing output and 
    #to ensure that when test_mode is True, the quiz is not run
    assert perform_quiz(True) == 'This is the test mode'
    assert perform_quiz(True) != 'This is not the test mode'
   
    #to ensure that the final Score is an integer value
    assert isinstance(Score, int)
    
    #to ensure that the Output is a string 
    assert isinstance(Output, str)
    
    #to ensure that the Output is empty when the quiz has not been completed
    assert Output ==''
    
    #to ensure that before the test, an appropriate response based on the score is given
    assert possible_score[Score] == possible_score[0]
    
def test_database():
    
    #to check if database is callable 
    assert callable(database)
    
    #to check if the test_mode gives desired testing output 
    #to ensure that when test_mode is True, the database is not run
    assert database(True) == 'This is a test mode'
    assert database(True) != weekly_cases
    assert database(True) != weekly_death
    assert database(True) != cases_age_group
    assert database(True) != imp_stats
    
    #to ensure that the output from the database is a dictionary 
    assert isinstance(weekly_cases, dict)
    assert isinstance(weekly_death, dict)
    assert isinstance(cases_age_group, dict)
    assert isinstance(imp_stats, dict)


                 
    