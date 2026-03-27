import pytest
from week_6_exercise_3 import sum_numbers_list

def test_sum_number_list_with_correct_parameter():
    #Arrange
    numbers_list = [2,6,23,78,54,16]

    #Act
    result = sum_numbers_list(numbers_list)

    #Assert
    assert result == 179

def test_sum_number_list_with_incorrect_parameter():
    #Arrange
    numbers_list = [2,"6",23,78,54,16] #one of the numbers in the list is a string

    #Act & Assert
    with pytest.raises(TypeError):
        result = sum_numbers_list(numbers_list)

def test_sum_number_list_with_empty_list():
    #Arrange
    numbers_list = []

    #Act
    result = sum_numbers_list(numbers_list)

    #Assert
    assert result == 0