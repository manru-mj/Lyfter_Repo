import pytest
from logic import FinanceManager

# testing Category
def test_add_category_success():

    # Arrange
    manager = FinanceManager()

    # Act
    manager.add_category(
        "Food",
        "#ff0000",
        "expense"
    )

    # Assert
    assert len(manager.categories) == 1
    assert manager.categories[0].name == "Food"


def test_duplicate_category():

    # Arrange
    manager = FinanceManager()

    manager.add_category(
        "Food",
        "#ff0000",
        "expense"
    )

    # Act / Assert
    with pytest.raises(ValueError):
        manager.add_category(
            "Food",
            "#ffffff",
            "expense"
        )


def test_invalid_category_type():

    # Arrange
    manager = FinanceManager()

    # Act / Assert
    with pytest.raises(ValueError):
        manager.add_category(
            "Crypto",
            "#00ff00",
            "investment"
        )


# Testing Amount Validation
def test_valid_amount():

    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.is_valid_amount("1500.50")

    # Assert
    assert result is True


def test_invalid_amount_letters():

    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.is_valid_amount("abc")

    # Assert
    assert result is False


def test_invalid_amount_zero():

    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.is_valid_amount("0")

    # Assert
    assert result is False


# Testing date validation
def test_valid_date():

    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.is_valid_date("01/01/2025")

    # Assert
    assert result is True


def test_invalid_future_date():

    # Arrange
    manager = FinanceManager()

    # Act
    result = manager.is_valid_date("01/01/2099")

    # Assert
    assert result is False


# Testing transactions
def test_expense_transaction_is_negative():

    # Arrange
    manager = FinanceManager()

    manager.add_category(
        "Food",
        "#ff0000",
        "expense"
    )

    # Act
    manager.add_transaction(
        "01/01/2025",
        "Burger",
        "100",
        "Food"
    )

    transaction = manager.transactions[0]

    # Assert
    assert transaction.amount == -100


def test_income_transaction_stays_positive():

    # Arrange
    manager = FinanceManager()

    manager.add_category(
        "Salary",
        "#00ff00",
        "income"
    )

    # Act
    manager.add_transaction(
        "01/01/2025",
        "January Salary",
        "2000",
        "Salary"
    )

    transaction = manager.transactions[0]

    # Assert
    assert transaction.amount == 2000


def test_transaction_without_category():

    # Arrange
    manager = FinanceManager()

    # Act / Assert
    with pytest.raises(ValueError):
        manager.add_transaction(
            "01/01/2025",
            "Burger",
            "100",
            ""
        )


#testing filters
def test_filter_by_category_type():

    # Arrange
    manager = FinanceManager()

    manager.add_category(
        "Salary",
        "#00ff00",
        "income"
    )

    manager.add_category(
        "Food",
        "#ff0000",
        "expense"
    )

    manager.add_transaction(
        "01/01/2025",
        "Salary January",
        "2000",
        "Salary"
    )

    manager.add_transaction(
        "02/01/2025",
        "Burger",
        "100",
        "Food"
    )

    # Act
    filtered = manager.filter_transactions(
        category_type="income"
    )

    # Assert
    assert len(filtered) == 1
    assert filtered[0].title == "Salary January"


def test_filter_by_start_date():

    # Arrange
    manager = FinanceManager()

    manager.add_category(
        "Salary",
        "#00ff00",
        "income"
    )

    manager.add_transaction(
        "01/01/2025",
        "January Salary",
        "2000",
        "Salary"
    )

    manager.add_transaction(
        "10/01/2025",
        "Bonus",
        "500",
        "Salary"
    )

    # Act
    filtered = manager.filter_transactions(
        start_date="05/01/2025"
    )

    # Assert
    assert len(filtered) == 1
    assert filtered[0].title == "Bonus"