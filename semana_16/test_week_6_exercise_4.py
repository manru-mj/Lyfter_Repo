import pytest
from week_6_exercise_4 import invert_string

def test_invert_string_with_correct_parameter():
    #Arrange
    new_string = "something new"

    #Act
    result = invert_string(new_string)

    #Assert
    assert result == "wen gnihtemos"

def test_invert_string_with_empty_string():
    #Arrange
    new_string = ""

    #Act
    result = invert_string(new_string)

    #Assert
    assert result == ""

def test_invert_string_with_incorrect_parameter():
    #Arrange
    new_string = 9857

#Act & Assert
    with pytest.raises(TypeError):
        result = invert_string(new_string)