from logic import FinanceManager, Transaction
import json
import csv
from datetime import datetime 

def save_data(manager_obj,filename): 
    main_dict = {} 
    
    c_list = [] 
    for category in manager_obj.categories: 
        c_list.append(category.to_dictionary()) 
    
    tr_list = [] 
    for transaction in manager_obj.transactions: 
        tr_list.append(transaction.to_dictionary()) 
    
    main_dict['categories'] = c_list 
    main_dict['transactions'] = tr_list 
    
    with open(filename,"w",encoding="utf-8") as data_file: 
        json.dump(main_dict, data_file, indent=4)


def load_data(filename):
    manager = FinanceManager()
    
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data_file = json.load(file)

        for category_dict in data_file.get("categories", []):
            cat_name = category_dict["name"]
            cat_color = category_dict["color"]
            cat_type = category_dict["type"]
            manager.add_category(cat_name,cat_color,cat_type)     
        
        for transaction_dict in data_file.get("transactions", []):
            tr_date = transaction_dict["date"]
            tr_title = transaction_dict["title"]
            tr_amount = transaction_dict["amount"]
            tr_category = transaction_dict["category"]
            category_name = tr_category["name"] 
            
            category_obj = manager._find_category(category_name)
            new_transaction = Transaction(tr_date, tr_title, tr_amount, category_obj)
            manager.transactions.append(new_transaction)

    except FileNotFoundError:
        return manager, "File not found"

    except json.JSONDecodeError:
        return manager, "File is corrupted"
    return manager, None


def export_to_csv(transactions, filename='Finance Report.csv'):
    
    total_income = 0
    total_expense = 0

    sorted_transactions = sorted(transactions, key=lambda t: datetime.strptime(t.date, "%d/%m/%Y"))

    with open(filename, 'w', newline='',encoding='utf-8-sig') as file:

        writer =  csv.writer(file)

        #headers list
        writer.writerow(['Date','Title','Amount','Category','Type'])

        #transactions list
        for t in sorted_transactions:

            #calculate totals
            if t.category.c_type == 'income':
                total_income += t.amount
            else:
                total_expense += t.amount

            writer.writerow([
                t.date,
                t.title,
                f'{t.amount:,.2f}',
                t.category.name,
                t.category.c_type.capitalize()
            ])

        #Balance
        net_balance = total_income + total_expense

        #let's have an empty row to separate transactions from balance
        writer.writerow([])

        # Totals
        writer.writerow(['Totals'])
        writer.writerow([f'Income: {total_income:,.2f}'])
        writer.writerow([f'Expenses: {total_expense:,.2f}'])
        writer.writerow([f'Net Balance: {net_balance:,.2f}'])

