import json
from pathlib import Path
from datetime import datetime


FILE_NAME = 'expense_list.json'

def load_expenses(file_name):
    """Load existing Expenses from the JSON file."""
    file_path = Path(file_name)
    if file_path.exists():
        try:
            with open(file_path, 'r')as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"expenses" : []}
    return {"expenses" : []}

def save_expenses(expenses,file_name):
    """Save all the expenses to the JSON file"""
    try:
        with open(file_name, 'w')as f:
            json.dump(expenses, f, indent=4)
        print(f"Data successfully saved to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")
        
        
        
def add_expense(expense_description, amount, file_name):
    expense_list = load_expenses(file_name)
    
    if expense_list['expenses']:
        next_id = max(expense['id'] for expense in expense_list['expenses']) + 1 
    else:
        next_id = 1
        
    # Create new expense
    new_expense = {
        'id' : next_id,
        'expense' : expense_description,
        'amount': amount,
        'date': datetime.now().strftime("%Y-%m-%d"), 
    }
    
    expense_list['expenses'].append(new_expense)
    
    save_expenses(expense_list, file_name)
    print(f"Expense added with ID: {new_expense['id']}")
    return new_expense['id']    

def update_expense(expense_id, new_description=None, new_amount=None, file_name=FILE_NAME):
    """ Update an existing expense by ID"""
    
    expense_list = load_expenses(file_name)
    
    for expense in expense_list['expenses']:
        if expense['id'] == expense_id:
            if new_description:
                expense['expense'] = new_description
            if new_amount is not None:
                if isinstance(new_amount, (int, float)):
                    expense['amount'] = new_amount
                else:
                    print("Error: Amount must be a number.")
                    return False
            save_expenses(expense_list, file_name)
            print(f"Expense {expense_id} updated successfully")
            return True
        
    print(f"Expense with ID {expense_id} not found")
    return False    


def delete_expense(expense_id, file_name=FILE_NAME):
    """Delete an expense by ID"""
    
    expense_list = load_expenses(file_name)
    
    # Find the index of the expense to delete
    for index, expense in enumerate(expense_list['expenses']):
        if expense['id'] == expense_id:
            expense_list['expenses'].pop(index)
            save_expenses(expense_list, file_name)
            print(f"Expense {expense_id} deleted successfully")
            return True
    
    print(f"Expense with ID {expense_id} not found")
    return False       
    
def summary_expenses(file_name=FILE_NAME):
    """Get the total amount of the expenses"""
    
    expense_list = load_expenses(file_name)
    net_total = 0
    
    for expense in expense_list['expenses']:
        if expense['amount']:
            net_total += expense['amount']
    print(f"Total expenses: ${net_total}")
    return True