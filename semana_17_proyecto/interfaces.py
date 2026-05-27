import FreeSimpleGUI as sg
from data_persistence import save_data, export_to_csv
from datetime import datetime   

file_name = "finance_data.json"

# Window to enter details of an expense and save it in a JSON file
def run_add_expense_window(manager):

    cat_list = []

    for names in manager.categories:
        if names.c_type == "expense":
            cat_list.append(names.name)

    sg.theme('black')

    expense_form_layout = [
        [sg.Text('Date',size=8),sg.Input(key='DATE',size=14,default_text='dd/mm/yyyy')],
        [sg.Text('Title',size=8),sg.Input(key='TITLE')],
        [sg.Text('Amount',size=8),sg.Input(key='AMOUNT')],
        [sg.Text('Category',size=8),sg.DropDown(key='CATEGORY',values=cat_list)],
        [sg.Button('Save Expense'),sg.Button('Close')],
    ]

    window = sg.Window("Expense Form",expense_form_layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break
        
        if event == 'Save Expense':
            try:
                manager.add_transaction(
                    values['DATE'],
                    values['TITLE'],
                    values['AMOUNT'],
                    values['CATEGORY']
                )
            
                save_data(manager,file_name)
                sg.popup("Expense added successfully!")

                window['DATE'].update('dd/mm/yyyy')
                window['TITLE'].update('')
                window['AMOUNT'].update('')
                window['CATEGORY'].update('')                
                window['DATE'].set_focus()

            except Exception as e:
                sg.popup(f"Error Message:{str(e)}")

    window.close()

# Window to enter details of an income and save it in a JSON file
def run_add_income_window(manager):

    cat_list = []

    for names in manager.categories:
        if names.c_type == "income":
            cat_list.append(names.name)

    sg.theme('black')

    expense_form_layout = [
        [sg.Text('Date',size=8),sg.Input(key='DATE',size=14,default_text='dd/mm/yyyy')],
        [sg.Text('Title',size=8),sg.Input(key='TITLE')],
        [sg.Text('Amount',size=8),sg.Input(key='AMOUNT')],
        [sg.Text('Category',size=8),sg.DropDown(key='CATEGORY',values=cat_list)],
        [sg.Button('Save Income'),sg.Button('Close')],
    ]

    window = sg.Window("Income Form",expense_form_layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break
        
        if event == 'Save Income':
            try:
                manager.add_transaction(
                    values['DATE'],
                    values['TITLE'],
                    values['AMOUNT'],
                    values['CATEGORY']
                )
            
                save_data(manager,file_name)
                sg.popup("Income added successfully!")

                window['DATE'].update('dd/mm/yyyy')
                window['TITLE'].update('')
                window['AMOUNT'].update('')
                window['CATEGORY'].update('')                
                window['DATE'].set_focus()                

            except Exception as e:
                sg.popup(f"Error Message:{str(e)}")

    window.close()

# Window to enter the details of a category and save it in a JSON file
def run_add_category_window(manager):

    cat_type_list = ["Income","Expense"]

    sg.theme('black')

    expense_form_layout = [
        [sg.Text('Name',size=12),sg.Input(key='NAME')],
        [sg.Text('Category Type',size=12),sg.DropDown(key='CATEGORY',values=cat_type_list,size=8),sg.ColorChooserButton('Select Color',target='COLOR',size=10),sg.Input(key='COLOR',size=8)],
        [sg.Button('Save Category',size=11),sg.Button('Close',size=11)],
    ]

    window = sg.Window("Category Form",expense_form_layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break
        
        if event == 'Save Category':
            try:
                manager.add_category(
                    values['NAME'],
                    values['COLOR'],
                    values['CATEGORY']
                )
            
                save_data(manager,file_name)
                sg.popup("Category added successfully!")
                #cleans the window fields and set focus back to date
                window['NAME'].update('')
                window['COLOR'].update('')
                window['CATEGORY'].update('')
                window['NAME'].set_focus()

            except Exception as e:
                sg.popup(f"Error Message:{str(e)}")

    window.close()    


# Main window to show the table and from where the other windows can be called 
def run_main_window(manager):

    headings = ['Date','Title','Amount','Category','Type']
    data, row_colors = build_table_data(manager.get_transactions())

    #to export what's visible in the table
    current_transactions = manager.get_transactions()

    category_names = []    
    #category_names.sort()

    sg.theme('black')

    layout = [
        [sg.Text('Start date:'),sg.Input(key='START_DATE',size=10, default_text='dd/mm/yyyy'),sg.Text('End date:'),sg.Input(key='END_DATE',size=10,default_text='dd/mm/yyyy'),sg.Text('Category Type:'),sg.DropDown(key='CATEGORY_TYPE',values=('','income','expense'),size=7,enable_events=True),sg.Text('Category Name:'),sg.DropDown(key='CATEGORY_NAME',values=category_names,size=10)],
        [sg.Table(
        values = data,
        headings = headings,
        auto_size_columns = True,
        num_rows = 14,
        background_color = 'white',
        text_color = 'black',   
        alternating_row_color = 'light gray',
        justification = 'left',
        row_colors = row_colors,
        key = 'TABLE',
        expand_x=True,
        expand_y=True)],
        [sg.Button('Add Category',key='ADD_CATEGORY'),sg.Button('Add Income',key='ADD_INCOME'),sg.Button('Add Expense',key='ADD_EXPENSE'),sg.Text("", size=(1, 1)),sg.Button('Run Filter',key='FILTER'),sg.Button('Export to CSV',key='EXPORT'),sg.Button('Close',key='CLOSE')]
    ]

    window = sg.Window("My Finance Manager", layout,resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'CLOSE':
            save_data(manager, file_name)
            break

        if event == 'ADD_CATEGORY':
            run_add_category_window(manager)
        
        if event == 'ADD_INCOME':            
            income_categories = manager.get_category_names_by_type('income')

            if len(income_categories) <= 1:
                sg.popup("Please create at least one income category first.")
            else:            
                run_add_income_window(manager)
                refresh_table(window,manager)
                current_transactions = manager.get_transactions()

        if event == 'ADD_EXPENSE':            
            income_categories = manager.get_category_names_by_type('expense')

            if len(income_categories) <= 1:
                sg.popup("Please create at least one expense category first.")
            else:            
                run_add_expense_window(manager)
                refresh_table(window,manager)
                current_transactions = manager.get_transactions()
        
        if event == 'CATEGORY_TYPE':
            category_names = manager.get_category_names_by_type(values['CATEGORY_TYPE'])
            window['CATEGORY_NAME'].update(values=category_names, value='')

        if event == 'FILTER':
            try:
                filtered = manager.filter_transactions(
                    values['START_DATE'],
                    values['END_DATE'],
                    values['CATEGORY_NAME'],
                    values['CATEGORY_TYPE']
                )
            
                data, row_colors = build_table_data(filtered)

                #to export what's visible in the table
                current_transactions = filtered

                window['TABLE'].update(
                    values=data,
                    row_colors=row_colors
                )
            except Exception as e:
                sg.popup(f"Filter Error: INVALID DATE!")
    
        if event == 'EXPORT':
            try:
                export_to_csv(current_transactions)
                sg.popup('CSV has been exported successfully!')
            
            except Exception as e:
                sg.popup(f'Export Error: {str(e)}')

    window.close()


def build_table_data(transactions):
    data = []
    row_colors = []

    #Sort transactions by date to show them in table
    sorted_transactions = sorted(transactions, key=lambda t: datetime.strptime(t.date, "%d/%m/%Y"))

    #Add transactions in rows for the list to be used in the table
    for index, c in enumerate(sorted_transactions):        
        row = []
        row.append(c.date)
        row.append(c.title)
        row.append(f"{c.amount:,.2f}")
        row.append(c.category.name)
        row.append(c.category.c_type)
        data.append(row)

        #Category Color
        background_color = c.category.color
        row_colors.append((index,'black',background_color))

    return data,row_colors


#this method is used to refresh the table when a new transaction is added
def refresh_table(window, manager):
    data, row_colors = build_table_data(manager.get_transactions())
    window['TABLE'].update(values=data, row_colors = row_colors)




# file_name = ("finance_data.json")
# manager, error = load_data(file_name)
# run_main_window(manager)



