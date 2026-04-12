import pytest
from week_6_exercise_5 import count_upper_lower

def test_count_upper_lower_with_correct_parameter():
    #Arrange
    new_string = "String With Initial Upper Cases"

    #Act
    upper, lower = count_upper_lower(new_string)

    #Assert
    assert upper == 5
    assert lower == 22

def test_count_upper_lower_with_empty_string():
    #Arrange
    new_string = ""

    #Act
    upper, lower = count_upper_lower(new_string)

    #Assert
    assert upper == 0
    assert lower == 0

def test_count_upper_lower_with_only_lower_cases():
    #Arrange
    new_string = "only lower"

    #Act
    upper, lower = count_upper_lower(new_string)

    #Assert
    assert upper == 0
    assert lower == 9