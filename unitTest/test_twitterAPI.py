import pytest
import twitterAPI

def test_for_missing_company_name(monkeypatch): 
  
  #monkeypatch the "input" function so that it returns "".
  #This simulates the user entereing nothing in the terminal. 
  monkeypatch.setattr('builtins.input', lambda_: ""
                      
  i = input("Please enter the name of the company you want to evaluate:")
  assert i = ""
