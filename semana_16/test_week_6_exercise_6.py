import pytest
from week_6_exercise_6 import *

def test_process_string_with_correct_parameter():
    #Arrange
    new_string = "String-With-Initial-Upper-Cases"

    #Act
    result = process_string(new_string)

    #Assert
    assert result == "Cases-Initial-String-Upper-With"

def test_convert_string_to_list():
    #Arrange, Act and Assert
    assert convert_string_to_list("b-a-c") == ["b", "a", "c"]

def test_convert_list_to_string():
    #Arrange, Act and Assert
    assert convert_list_to_string(["b", "a", "c"]) == "a-b-c"