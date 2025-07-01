from bankAccount import BankAccount,SavingsAccount
from menu import Menu


menu_tile = "\nSelect an option:"
menu_options = ["1. Open Savings Account",
        "2. Deposit",
        "3. Withdraw",
        "4. Show Balance",
        "5. Exit"]

new_account = SavingsAccount(0)

if __name__ == "__main__":
    new_menu = Menu(menu_tile,menu_options,len(menu_options))
    is_running = True
    amount = 0

    while is_running:
        option = new_menu.select_option()

        if option == 1:
            min_balance = float(input("Please type the intial deposit, this will be the minimum amount to be maintained: "))
            new_account = SavingsAccount(min_balance)
        elif option == 2:
            amount = float(input("Please type the amount to be deposited: "))
            new_account.deposit(amount)
            new_account.print_balance()
        elif option == 3:
            amount = float(input("Please type the amount to be withdrawn: "))
            new_account.withdraw(amount)
            new_account.print_balance()
        elif option == 4:
            new_account.print_balance()
        elif option == 5:
            print("You have selected to exit. Goodbye!")
            is_running = False