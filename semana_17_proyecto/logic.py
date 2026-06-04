from datetime import datetime 

class Category:
    def __init__(self, name:str, color:str , c_type:str):
        self.name = name
        self.color = color
        self.c_type = c_type

    def to_dictionary(self):
        return {'name': self.name,
                'color': self.color,
                'type' : self.c_type
                }


class Transaction:
    def __init__(self, date:str, title:str, amount:float, category:Category):
        self.date = date
        self.title = title
        self.amount = amount
        self.category = category


    def to_dictionary(self):
        return {
            'date': self.date,
            'title': self.title,
            'amount': self.amount,
            'category': self.category.to_dictionary()
        }

class FinanceManager:
    def __init__(self):
        self.categories = []
        self.transactions = []


    def add_category(self,name:str, color:str,c_type:str):
        name = name.strip()
        if name == '':
            raise ValueError('Category name cannot be empty')

        color = color
        c_type = c_type.strip().lower()
        if c_type == '':
            raise ValueError('Please select a category type')
        
        if c_type not in ("expense", "income"):
            raise ValueError("Invalid category type")

        #validates category is not already existing
        if not self._find_category(name):
            new_category = Category(name,color,c_type)
            self.categories.append(new_category)
        else:
            raise ValueError("Category already exists")


    def _find_category(self, name:str):
        for category in self.categories:
            #compares entry with existing category ignoring case or mistyped spaces
            if category.name.strip().lower() == name.strip().lower():
                return category
        return None


    def is_valid_amount(self, value):
        try:
            amount = float(value) 
            #validates amount is not 0
            if amount == 0:
                return False
            return round(amount, 2) == amount
        
        # if entry is not a number - invalid amount 
        except ValueError:
            return False


    def is_valid_date(self, date_string:str):
        try:
            #convert typed string into a date object
            date_object = datetime.strptime(date_string,"%d/%m/%Y").date()

            #Compare the entry with today's date 
            if date_object > datetime.now().date():
                return False
            
            return True
        except ValueError:
            return False


    def add_transaction(self, date: str, title: str, amount: str, category: str):
        title = title.strip()
        if title == '':
            raise ValueError('Transaction title cannot be empty')

        category = category.strip()
        category_obj = self._find_category(category)

        #Validate Date
        if not self.is_valid_date(date):
            raise ValueError("Invalid date format or future date")

        #Validate Category
        if category == '':
            raise ValueError("Please select a Category from the list")

        #Validate Amount
        if not self.is_valid_amount(amount):
            raise ValueError("Invalid amount")

        #convert amount to float number
        amount = round(float(amount), 2)

        #Evaluates the transaction type to assign negative value to expenses
        if category_obj.c_type == "expense":
            amount *= -1

        # Adds new transaction
        new_transaction = Transaction(date, title, amount, category_obj)
        self.transactions.append(new_transaction)


    def get_transactions(self):
        return self.transactions

    def get_category_names_by_type(self,category_type=None):
        
        category_type = category_type.lower() if category_type else None
        category_names = [""]

        for c in  self.categories:
            if category_type is None or c.c_type == category_type:
                category_names.append(c.name)
        
        return category_names

    def filter_transactions(self, start_date=None, end_date=None, category_name=None, category_type=None):
        
        # Ignore placeholder text
        #if start_date == 'dd/mm/yyyy':
        #    start_date = ''

        #if end_date == 'dd/mm/yyyy':
        #    end_date = ''
        
        #list of filtered transactions
        filtered = []

        for t in self.transactions:
            # Convert date from text to date type
            t_date = datetime.strptime(t.date, "%d/%m/%Y")

            # Evaluate Start date
            if start_date:
                start = datetime.strptime(start_date, "%d/%m/%Y")
                if t_date < start:
                    continue

            # Evaluate Start date
            if end_date:
                end = datetime.strptime(end_date, "%d/%m/%Y")
                if t_date > end:
                    continue

            # Evaluate Category name
            if category_name:
                if t.category.name != category_name:
                    continue

            if category_type:
                if t.category.c_type != category_type:
                    continue

            # if passed all filters
            filtered.append(t)

        return filtered    

