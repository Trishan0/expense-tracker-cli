import json
from pathlib import Path
from datetime import datetime
import calendar

# File to store expenses
FILE_NAME = 'expense_list.json'

def load_expenses(file_name):
    """Load existing expenses from the JSON file."""
    file_path = Path(file_name)
    if file_path.exists():
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"expenses": []}  # Return an empty structure if JSON is corrupted
    return {"expenses": []}  # Return an empty structure if file does not exist

def save_expenses(expenses, file_name):
    """Save all the expenses to the JSON file."""
    try:
        with open(file_name, 'w') as f:
            json.dump(expenses, f, indent=4)
        print(f"Data successfully saved to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def add_expense(expense_description, amount, file_name):
    """Add a new expense to the JSON file."""
    expense_list = load_expenses(file_name)
    
    # Assign a unique ID to the new expense
    if expense_list['expenses']:
        next_id = max(expense['id'] for expense in expense_list['expenses']) + 1 
    else:
        next_id = 1
    
    # Create new expense entry
    new_expense = {
        'id': next_id,
        'expense': expense_description,
        'amount': amount,
        'date': datetime.now().strftime("%Y-%m-%d"), 
    }
    
    # Append the new expense and save
    expense_list['expenses'].append(new_expense)
    save_expenses(expense_list, file_name)
    print(f"Expense added with ID: {new_expense['id']}")
    return new_expense['id']

def update_expense(expense_id, new_description=None, new_amount=None, file_name=FILE_NAME):
    """Update an existing expense by its ID."""
    expense_list = load_expenses(file_name)
    
    for expense in expense_list['expenses']:
        if expense['id'] == expense_id:
            # Update description if provided
            if new_description:
                expense['expense'] = new_description
            # Update amount if provided and valid
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
    """Delete an expense by its ID."""
    expense_list = load_expenses(file_name)
    
    # Find and remove the expense by ID
    for index, expense in enumerate(expense_list['expenses']):
        if expense['id'] == expense_id:
            expense_list['expenses'].pop(index)
            save_expenses(expense_list, file_name)
            print(f"Expense {expense_id} deleted successfully")
            return True
    
    print(f"Expense with ID {expense_id} not found")
    return False  
    
def view_all_expenses(file_name=FILE_NAME):
    """Display all recorded expenses."""
    expenses_list = load_expenses(file_name)
    
    if not expenses_list['expenses']:
        print("No expenses found!\nPlease add an expense first.")
        return
    
    # Print header
    print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<10}")
    print("-" * 45)
    
    # Print each expense
    for expense in expenses_list['expenses']:
        print(f"{expense['id']:<4} {expense['date']:<12} {expense['expense']:<15} ${expense['amount']:<10}")

def summary_expenses(file_name=FILE_NAME):
    """Calculate and display the total amount of all expenses."""
    expense_list = load_expenses(file_name)
    total_amount = sum(expense['amount'] for expense in expense_list['expenses'])
    print(f"Total expenses: ${total_amount}")
    return True

def month_summary(file_name=FILE_NAME, month=None):
    """Get the total expenses for a specific month."""
    expense_list = load_expenses(file_name)
    
    # Filter expenses for the given month
    month_expenses = [expense for expense in expense_list['expenses'] if datetime.strptime(expense['date'], "%Y-%m-%d").month == int(month)]
    
    if not month_expenses:
        print(f"No expenses found for {calendar.month_name[int(month)]}")
        return
    
    total_amount = sum(expense['amount'] for expense in month_expenses)
    print(f"Total expenses for {calendar.month_name[int(month)]}: ${total_amount}")
    return True

def month_expense(file_name=FILE_NAME, month=None):
    """Display all expenses of a specific month."""
    expense_list = load_expenses(file_name)
    
    # Filter expenses for the given month
    month_expenses = [expense for expense in expense_list['expenses'] if datetime.strptime(expense['date'], "%Y-%m-%d").month == int(month)]
    
    if not month_expenses:
        print(f"No expenses found for {calendar.month_name[int(month)]}")
        return
    
    # Print header
    print(f"Expenses for {calendar.month_name[int(month)]}:")
    print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<10}")
    print("-" * 45)
    
    # Print each expense
    for expense in month_expenses:
        print(f"{expense['id']:<4} {expense['date']:<12} {expense['expense']:<15} ${expense['amount']:<10}")
