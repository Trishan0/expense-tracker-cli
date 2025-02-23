import argparse as arg
from expense_tracker.methods import (
    add_expense, update_expense, delete_expense, summary_expenses,
    view_all_expenses, month_expense, month_summary, FILE_NAME
)

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
  expense-tracker delete --id 1
"""
    )

    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # Add expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", "-d", required=True, help="Expense description")
    add_parser.add_argument("--amount", "-a", required=True, type=float, help="Expense amount")
    add_parser.set_defaults(func=lambda args: add_expense(args.description, args.amount, FILE_NAME))

    # Update expense
    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("--id", required=True, type=int, help="Expense ID")
    update_parser.add_argument("--description", "-d", help="New description")
    update_parser.add_argument("--amount", "-a", type=float, help="New amount")
    update_parser.set_defaults(func=lambda args: (
        parser.error("Provide either --description or --amount to update")
        if not (args.description or args.amount)
        else update_expense(args.id, args.description, args.amount, FILE_NAME)
    ))

    # Delete expense
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", required=True, type=int, help="Expense ID")
    delete_parser.set_defaults(func=lambda args: delete_expense(args.id, FILE_NAME))

    # List expenses
    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.add_argument("--month", "-m", type=int, choices=range(1, 13), help="Filter by month (1-12)")
    list_parser.set_defaults(func=lambda args: month_expense(FILE_NAME, args.month) if args.month else view_all_expenses(FILE_NAME))

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", "-m", type=int, choices=range(1, 13), help="Show summary for a specific month (1-12)")
    summary_parser.set_defaults(func=lambda args: month_summary(FILE_NAME, args.month) if args.month else summary_expenses(FILE_NAME))

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
