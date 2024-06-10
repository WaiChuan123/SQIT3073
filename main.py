from functions import verify_user, calculate_tax, save_to_csv, read_from_csv
import pandas as pd

user_database = []

def main():

    filename = 'tax_records.csv'

    # Prompt the user to register or log in
    print("\nWelcome to the Malaysian Tax Input Program")

    # Choose the option to either register account, login account or exit the program
    while True:
        print("\nPlease choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1 or 2 or 3): ")

        # Choose 1 to register account
        if choice == '1':
            user_id = input("Enter your user ID: ")
            user_exists = False

            # User ID cannot be empty
            if not user_id:
                print("User ID cannot be empty. Please try again.")
                break
            
            # Cannot use User ID that has been registered
            for user_info in user_database:
                if user_info['User ID'] == user_id:
                    print("User ID already exists. Please choose a different User ID.")
                    user_exists = True
                    break

            # Enter 12 digits IC number and last 4 digits IC number    
            if not user_exists:
                ic_number = input("Enter your IC number (12 digits): ")
                
                if not ic_number:
                    print("IC Number cannot be empty. Please try again.")
                elif not ic_number.isdigit() or len(ic_number) != 12:
                    print("Invalid IC number. It must be exactly 12 digits.")
                else:
                    password = ic_number[-4:]
                    user_database.append({'User ID': user_id, 'IC': ic_number, 'Password': password})
                    print("User registered successfully!")
                    print("")
                    password = input("Enter your password (last 4 digits of your IC Numbers): ")

                    for user_info in user_database:
                            ic = user_info['IC']
                            max_attempts = 3  # Maximum number of login attempts allowed
                            attempts = 0
                            while attempts < max_attempts:
                                if verify_user(ic, password):
                                    print("Login successful!")
                                    break
                                else:
                                    attempts += 1
                                    remaining_attempts = max_attempts - attempts
                                    print(f"Invalid credentials. {remaining_attempts} attempts remaining.")

                                    if remaining_attempts > 0:
                                        password = input("Enter your password (last 4 digits of your IC number): ")
                                    else:
                                        print("Maximum login attempts reached. ")
                                        return
                    break
        
        # Choose 2 to login account
        elif choice == '2':
            user_id = input("Enter your User ID: ")
            
            # User ID cannot be empty
            if not user_id:
                print("User ID cannot be empty. Please try again.")
                continue
            
            # Enter last 4 digits IC number
            password = input("Enter your password (last 4 digits of your IC number): ")
            if not password:
                print("Password cannot be empty. Please try again.")
                continue
            user_found = False

            for user_info in user_database:
                if user_info['User ID'] == user_id:
                    ic_number = user_info['IC']
                    user_found = True
                    max_attempts = 3  # Maximum number of login attempts allowed
                    attempts = 0
                    while attempts < max_attempts:
                        if verify_user(ic_number, password) :
                            print("Login successful!")
                            break

                        else:
                            attempts += 1
                            remaining_attempts = max_attempts - attempts
                            print(f"Invalid credentials. {remaining_attempts} attempts remaining.")

                            if remaining_attempts > 0:
                                password = input("Enter your password (last 4 digits of your IC number): ")
                            else:
                                print("Maximum login attempts reached. ")
                                return
                            
                if not user_found:
                    print("User ID not found. Please register first.")
            
            if user_found:
                break
            
        # Choose 3 to exit program    
        elif choice == '3':
            exit()

        else:
            print("Invalid choice. Please try agian")
            continue

    print("\nWelcome to Main Menu of the Malaysian Tax Input Program")
    
    # Choose the option to either calculate tax, view tax records or back to login/ register page
    while True:
        print("\nMain Menu:")
        print("1. Calculate Tax")
        print("2. View Tax Records")
        print("3. Back")
        print("")

        option = input("Enter your choice (1-3): ")
        
        # Choose 1 to calculate the tax
        if option == '1':
            try:
                
                # Enter annual income
                annual_income = float(input("Enter your annual income: RM "))
                
                # Choose tax relief based on personal situation
                tax_reliefs = {
                    'Individual': 0,
                    'Spouse': 0,
                    'Child': 0,
                    'Medical Expenses': 0,
                    'Lifestyle': 0,
                    'Education Fees': 0,
                    'Parental Care': 0
                }

                is_resident = input("Are you a resident individual taxpayer? (yes/no): ").strip().lower()
                if is_resident == 'yes':
                    tax_reliefs['Individual'] = 9000

                spouse_income = float(input("Enter your spouse's annual income (0 if no income): RM "))
                if spouse_income <= 4000:
                    tax_reliefs['Spouse Relief'] = 4000

                children = int(input("Enter the number of children: "))
                tax_reliefs['Child Relief'] = min(children, 12) * 8000

                medical_expenses = float(input("Enter the amount of serious medical treatment expenses: RM "))
                tax_reliefs['Medical Expenses Relief'] = min(medical_expenses, 8000)

                lifestyle_expenses = float(input("Enter the amount of lifestyle-related expenses: RM "))
                tax_reliefs['Lifestyle Relief'] = min(lifestyle_expenses, 2500)

                education_fees = float(input("Enter the amount of education fees: RM "))
                tax_reliefs['Education Fees Relief'] = min(education_fees, 7000)

                parental_care_expenses = float(input("Enter the amount of parental care expenses: RM "))
                tax_reliefs['Parental Care Relief'] = min(parental_care_expenses, 5000)

            except ValueError:
                print("Invalid input for income or tax relief.")
                continue

            total_reliefs = sum(tax_reliefs.values())
            tax_payable = calculate_tax(annual_income, total_reliefs)
            print(f"\nTotal reliefs: RM {(total_reliefs):.2f}")
            print(f"Your calculated tax payable is: RM {tax_payable:.2f}")

            user_data = {
                'IC Number': ic_number,
                'Annual Income': annual_income,
                'Tax Relief': total_reliefs,
                'Tax Payable': tax_payable
            }

            save_to_csv(user_data, filename)
            print("Data saved successfully.")

        # Choose 2 to view tax records
        elif option == '2':
            data = read_from_csv(filename)
            if data is not None:
                print("\nTax Records:")
                print(data)
            else:
                print("No tax records found.")

        # Choose 3 to come back to login/ register page
        elif option == '3':
            main()
        else:
            print("Invalid choice. Please choose again.")
            continue

if __name__ == "__main__":
    main()