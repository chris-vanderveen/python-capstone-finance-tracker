VALID_OPTIONS = [1, 2, 3, 4]

def display_menu() -> int:
    """Displays menu, takes user input and performs input sanitization.

    Returns:
        An int representing the option the user has chosen.
    """

    while True:
        option = input("\nWhat would you like to do?\n1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit\nChoose an option: ")

        try:
            option_int = int(option)
            if option_int in VALID_OPTIONS:
                # Valid option
                return option_int
            else:
                # User entered invalid integer
                print(f"\n{option_int} is not a valid option. Please enter an integer between {VALID_OPTIONS[0]} and {VALID_OPTIONS[-1]}.")
        except ValueError:
            # Input couldn't be cast to int
            print(f"\n{option} is not a valid choice. Please enter an integer between {VALID_OPTIONS[0]} and {VALID_OPTIONS[-1]}.")

def add_expense(data: dict[str, list[tuple[str, float]]]) -> None:
    """Prompts the user for expense description, category, and adds them to an expense dictionary.

        Args:
            data: Dictionary of expenses with categories (str) as keys and a list of tuples: (str, float) representing expense description and value respectively. 
    """

    while True:
        # Loop to receive usier input
        description = input("Enter expense description: ")
        category = input("Enter expense category: ")
        # Need to check if category exists already or not
        amount = input("Enter expense amount: ")

        try:
            amount = float(amount)
            if category in data.keys():
                data[category].append((description, amount))
                break
            else:
                data[category] = [(description, amount)]
                break
        except ValueError:
            # Amount could not be cast to float
            print(f"\n{amount} is not a valid amount. Please enter a number.")

    print("\nExpense Added Successfully.")

def view_expenses(data: dict[str, list[tuple]]) -> None:
    """Displays all categories and their respective expenses."""

    print()
    if len(data) <= 0:
        print("Expense tracker is empty. Please enter some items to view expenses.")
    else:
        for key in data.keys():
            print(f"Category: {key}")
            for value in data[key]:
                print(f"\t- {value[0]}: ${value[1]:.2f}")

def view_summary(data: dict[str, list[tuple]]) -> None:
    "Calculates totals for each category and displays a summary."

    if len(data) <= 0:
        print("\nExpense Tracker is empty. Please add some items to view a summary.")
    else:
        print("\nSummary: ")
        for key in data.keys():
            total = 0
            for value in data[key]:
                total += value[1]

            print(f"{key}: ${total:.2f}")
            
def pft():
    """Main driver fucntion for the Personal Finance Tracker"""

    print("Welcome to the Personal Finance Tracker!")

    data = {}
    option = 0

    while option != 4:
        option = display_menu()

        match option:
            case 1:
                # Add expense option selected
                add_expense(data)
                print(data)
            case 2:
                # View all expenses option selected
                view_expenses(data)
            case 3:
                # View summary option selected
                view_summary(data)
            case 4:
                pass
            case _:
                print("An unexpected error occurred with the menu choice. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    pft()
