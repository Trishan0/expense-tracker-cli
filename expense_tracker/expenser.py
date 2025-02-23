import argparse as arg
from expense_tracker.methods import add_expense, update_expense, delete_expense, summary_expenses, view_all_expenses,month_expense, month_summary, FILE_NAME
def main():
    
    parser = arg.ArgumentParser(
        description="Track and manage expenses",
        formatter_class=arg.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  expense-tracker add --description "Lunch" --amount 20
  expense-tracker list
  expense-tracker summary --month 8
  expense-tracker update --id 1 --description "Dinner" --amount 25
  expense-tracker delete --id 1""")

    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # add expenses commands
    add_parser = subparsers.add_parser('add', help="Add a new expense")
    add_parser.add_argument('--description', '-d', required=True, help="Expense description")
    add_parser.add_argument('--amount', '-a', required=True, type=float, help="Expense amount")

    # update expenses commands
    update_parser = subparsers.add_parser('update', help="Update an existing expense")
    update_parser.add_argument('--id', required=True, type=int, help="Expense ID")
    update_parser.add_argument('--description', '-d', help="New description")
    update_parser.add_argument('--amount', '-a', type=float, help="New amount")

 # Delete expense
    delete_parser = subparsers.add_parser('delete', help="Delete an expense")
    delete_parser.add_argument('--id', required=True, type=int, help="Expense ID")

    # List expenses
    list_parser = subparsers.add_parser('list', help="List all expenses")
    list_parser.add_argument('--month', '-m', type=int, choices=range(1, 13),
                            help="Filter by month (1-12)")

    # Summary
    summary_parser = subparsers.add_parser('summary', help="Show expense summary")
    summary_parser.add_argument('--month', '-m', type=int, choices=range(1, 13),
                              help="Show summary for specific month (1-12)")
    
    
    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args.description, args.amount, FILE_NAME)

    elif args.command == 'update':
        if not (args.description or args.amount):
            print("Please provide either new description or amount to update")
            return
        update_expense(args.id,args.description, args.amount)
        
    elif args.command == 'delete':
        delete_expense(args.id)
    
    elif args.command == 'list':
        if args.month:
            month_expense(FILE_NAME, int(args.month))
        else:
            view_all_expenses(FILE_NAME)
    
    elif args.command == 'summary':
        if args.month:
            month_summary(FILE_NAME, int(args.month))
        else:
            summary_expenses()          
     
    else:
        parser.print_help()
        