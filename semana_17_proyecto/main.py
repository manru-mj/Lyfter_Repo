from interfaces import run_main_window
from data_persistence import load_data

file_name = "finance_data.json"

manager, error = load_data(file_name)

if error:
    print(error)

run_main_window(manager)