
expense_list=[]

def empty():
    print("Your expense tracker is empty")
    print("Please add expenses first!")

def display_menu():
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Category Summary")
    print("5. Highest Expenses")
    print("6. Lowest Expenses")
    print("7. Monthly Total")
    print("8. Delete Expenses")
    print("9. Exit")

def add_expense():
    print("======= ADD EXPENSES =======", end="\n\n")
    while True:
        id_input = input("Enter expense id: ").strip()
        if id_input.isdigit():
            expense_id = int(id_input)
            id_exist = False
            for exp in expense_list:
                if exp["Expense ID"] == expense_id:
                    id_exist = True
                    break
            if id_exist:
                print("Error! Entered id is already in the list")
            else:
                break
        else:
            print("Enter valid id!")

    expense_category = input("Enter category: ").strip()
    expense_description = input("Enter description: ").strip()

    while True:
        amount_input = input("Enter amount: ").strip()
        if amount_input.isdigit():
            expense_amount = int(amount_input)
            if expense_amount <= 0:
                print("Error! Amount must be greater than zero.")
            else:
                break
        else:
            print("Enter valid amount")

    while True:
        expense_date = input("Enter date (DD/MM/YYYY): ").strip()
        if len(expense_date)==10 and expense_date[2]=="/" and expense_date[5]=="/":
            day_part=expense_date[0:1]
            month_part=expense_date[3:5]
            year_part=expense_date[6:10]
            if day_part.isdigit() and month_part.isdigit() and year_part.isdigit():
                day_num=int(day_part)
                month_num=int(month_part)
                year_num=int(year_part)
                if (1<day_num<31) and (1<month_num<12) and year_num>0:
                    break
                else:
                    print("Invalid date values:(Day 1-31,Month 1-12,Year greater than 0.)")
            else:
                print("Invalid input!Give numbers for date.")
        else:
            print("Invalid date format!Enter like DD/MM/YYYY.")
                
    expense_dict = {
        "Expense ID": expense_id,
        "Expense Category": expense_category,
        "Expense Description": expense_description,
        "Expense Amount": expense_amount,
        "Expense Date": expense_date
    }
    print()
    expense_list.append(expense_dict)
    
    print("Expenses added successfully!", end="\n\n")

def view_expense():
    if expense_list == []:
        empty()
    else:
        print("======= ALL EXPENSES =======")
        for exp in expense_list:
            print("ID:", exp["Expense ID"])
            print("Category:", exp["Expense Category"])
            print("Description:", exp["Expense Description"])
            print("Amount:", "₹", exp["Expense Amount"])
            print("Date:", exp["Expense Date"], end="\n\n")
        print(f"Total number of expenses: {len(expense_list)}")

def search_category():
    search_input = input("Enter category to search: ").strip().lower()
    matches = [exp for exp in expense_list if search_input in exp["Expense Category"].lower()]
    
    if not matches:
        print(f"No matching category found for '{search_input}'!\n")
    else:
        print("Matching expenses:")
        for exp in matches:
            print(f"{exp['Expense Category']} - {exp['Expense Description']} - ₹{exp['Expense Amount']}")
        print()

def search_description():
    search_input = input("Enter description to search: ").strip().lower()
    matches = [exp for exp in expense_list if search_input in exp["Expense Description"].lower()]
    
    if not matches:
        print(f"No matching description found for '{search_input}'!\n")
    else:
        print("Matching expenses:")
        for exp in matches:
            print(f"{exp['Expense Category']} - {exp['Expense Description']} - ₹{exp['Expense Amount']}")
        print()

def search_id():
    search_input = input("Enter expense ID to search: ").strip()
    if search_input.isdigit():
        search_id_val = int(search_input)
        matches = [exp for exp in expense_list if exp["Expense ID"] == search_id_val]
        if not matches:
            print("No matching expense ID found!\n")
        else:
            print("Matching expenses:")
            for exp in matches:
                print(f"ID: {exp['Expense ID']} | {exp['Expense Category']} - {exp['Expense Description']} - ₹{exp['Expense Amount']}")
            print()
    else:
        print("Enter valid ID!\n")

def search_expense():
    if expense_list == []:
        empty()
    else:
        search = True
        while search:
            print("1. Search by ID")
            print("2. Search by Category")
            print("3. Search by Description")
            choice_input = input("Enter your choice option: ").strip()
            if choice_input.isdigit():
                choice = int(choice_input)
                if choice == 1:
                    search_id()
                    search = False
                elif choice == 2:
                    search_category()
                    search = False
                elif choice == 3:
                    search_description()
                    search = False
                else:
                    print("Choose a valid option between 1 and 3!\n")
            else:
                print("Enter a valid number!\n")
        
def category_summary():
    if expense_list == []:
        empty()
    else:
        print("========== CATEGORY SUMMARY ==========")
        summary = {}
        for exp in expense_list:
            cat = exp["Expense Category"]
            summary[cat] = summary.get(cat, 0) + exp["Expense Amount"]

        total_expense = 0
        for cat, total in summary.items():
            print(f"{cat}: ₹{total}")
            total_expense += total

        print(f"\nTotal Expense: ₹{total_expense}\n")

def highest_expense():
    if expense_list == []:
        empty()
    else:
        print("========== HIGHEST EXPENSE ==========")
        highest=expense_list[0]
        for exp in expense_list:
            if exp["Expense Amount"]>highest["Expense Amount"]:
                highest=exp
        print(f"Expense ID: {highest['Expense ID']}")
        print(f"Category: {highest['Expense Category']}")
        print(f"Description: {highest['Expense Description']}")
        print(f"Amount: ₹{highest['Expense Amount']}\n")

def lowest_expense():
    if expense_list == []:
        empty()
    else:
        print("========== LOWEST EXPENSE ==========")
        lowest=expense_list[0]
        for exp in expense_list:
            if exp["Expense Amount"]<lowest["Expense Amount"]:
                lowest=exp
        print(f"Expense ID: {lowest['Expense ID']}")
        print(f"Category: {lowest['Expense Category']}")
        print(f"Description: {lowest['Expense Description']}")
        print(f"Amount: ₹{lowest['Expense Amount']}\n")

def monthly_total():
    if expense_list == []:
        empty()
    else:
        print("========== MONTHLY REPORT ==========")
        while True:
            month_year = input("Enter month (MM/YYYY): ").strip()
            if len(month_year)==7 and "/" in month_year:
                month_part=month_year[0:2]
                year_part=month_year[3:7]
                if month_part.isdigit() and year_part.isdigit():
                    month_num=int(month_part)
                    if 1<=month_num<=12:
                        break
            else:
                print("Invalid format of input!")
                return
        total_amount=0
        expense_found=True
        for exp in expense_list:
            if exp["Expense Date"][3:10]==month_year:
                total_amount+=exp["Expense Amount"]
                print("Total spend in",month_year,":",total_amount)
                expense_found=False
                break
            if expense_found==False:
                print("No expense found for the period",month_year)

def delete_expense():
    if expense_list == []:
        empty()
    else:
        print("--- Delete Expense ---")
        id_input = input("Enter Expense ID to delete: ").strip()
        if id_input.isdigit():
            expense_id = int(id_input)
            for i, exp in enumerate(expense_list):
                if exp["Expense ID"] == expense_id:
                    del expense_list[i]
                    print("Expense deleted successfully!\n")
                    return
            print("Expense not found.\n")
        else:
            print("Enter valid ID!\n")

track = True
while track:
    display_menu()
    choice_input = input("\nEnter your choice: ").strip()
    print()
    if choice_input.isdigit():
        choice = int(choice_input)
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            search_expense()
        elif choice == 4:
            category_summary()
        elif choice == 5:
            highest_expense()
        elif choice == 6:
            lowest_expense()
        elif choice == 7:
            monthly_total()
        elif choice == 8:
            delete_expense()
        elif choice == 9:
            print("Thank you for using Expense Tracker!")
            track = False
        else:
            print("Choose a valid option between 1 and 9!")
    else:
        print("Please enter a valid number!")