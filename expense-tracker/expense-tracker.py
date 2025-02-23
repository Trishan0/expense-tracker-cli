import argparse as arg
from methods import add_expense, update_expense, delete_expense, summary_expenses, view_all_expenses,month_expense, month_summary, FILE_NAME
def main():
    
    parser = arg.ArgumentParser(
        description="Capture and save expenses to a JSON file")

    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # add expenses commands
    add_parser = subparsers.add_parser('add', help="Add a new expense")
    add_parser.add_argument('--description','-d',type=str, help="Expense Description")
    add_parser.add_argument('--amount', '-a', type=int, help="Cost of the expense")

    # update expenses commands
    update_parser = subparsers.add_parser('update', help="Update an existing expense")
    update_parser.add_argument('--id',type=int, help="Expense ID")
    update_parser.add_argument('--description','-d',type=str, help="New Description")
    update_parser.add_argument('--amount', '-a', type=int, help="New cost of the expense")

    # Delete expenses command
    delete_parser = subparsers.add_parser('delete', help="Delete an Expense")
    delete_parser.add_argument('--id', required=True, type=int, help='ID of the expense to delete')

    # List all expenses command
    view_parser = subparsers.add_parser('list', help="View all the expenses")
    view_parser.add_argument('--month', '-m', type=int)

    summary_parser = subparsers.add_parser('summary', help="Summary of Expenses")
    summary_parser.add_argument('--month','-m', help="Get a summary of specifi month by month number")
    
    
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
        
main()