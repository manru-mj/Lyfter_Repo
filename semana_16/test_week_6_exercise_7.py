import pytest
from week_6_exercise_7 import *

def test_create_prime_list_normal():
    #Arrange
    main_list = [1,2,3,4,5,6,7,8,9]
    #Act
    result = create_prime_list(main_list)
    #Assert
    assert result == [2,3,5,7]


def test_create_prime_list_no_primes():
    #Arrange
    main_list = [4,6,8,9,10,12,14,20]
    #Act
    result = create_prime_list(main_list)
    #Assert
    assert result == []

def test_create_prime_list_empty():
    #Arrange
    main_list = []
    #Act
    result = create_prime_list(main_list)
    #Assert
    assert result == []