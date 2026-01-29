class BankAccount:
    
    def __init__(self, account_holder, account_number, initial_balance=0.0):

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Successfully deposited ₱{amount:.2f}")
        return self.balance
    
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount != int(amount):
            raise ValueError("Withdrawal amount must be a whole number. ATMs only dispense bills.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Available balance: ₱{self.balance:.2f}")
        
        self.balance -= amount
        print(f"Successfully withdrew ₱{amount:.2f}")
        return self.balance
    
    def get_balance(self):

        return self.balance
    
    def display_account_info(self):

        print("\n" + "=" * 40)
        print("       ACCOUNT INFORMATION")
        print("=" * 40)
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₱{self.balance:.2f}")
        print("=" * 40)


def get_valid_amount(prompt):

    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Error: Amount cannot be negative. Please try again.")
                continue
            return amount  # Zero allowed here for initial balance; deposit/withdraw handle their own validation
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def main():

    print("\n" + "=" * 50)
    print("    WELCOME TO THE BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 50)
    
    # Get account holder information
    while True:
        try:
            name = input("\nEnter account holder name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            if not all(c.isalpha() or c.isspace() for c in name):
                raise ValueError("Name should only contain letters and spaces.")
            break
        except ValueError as e:
            print(f"Error: {e} Please try again.")
    
    while True:
        try:
            account_number = input("Enter account number: ").strip()
            if not account_number:
                raise ValueError("Account number cannot be empty.")
            if not account_number.isdigit():
                raise ValueError("Account number should only contain numbers.")
            break
        except ValueError as e:
            print(f"Error: {e} Please try again.")
    
    # Get initial balance
    initial_balance = get_valid_amount("Enter initial balance: ₱")
    
    # Create the bank account
    try:
        account = BankAccount(name, account_number, initial_balance)
        print(f"\nAccount created successfully for {name}!")
    except ValueError as e:
        print(f"Error creating account: {e}")
        return
    
    # Main menu loop
    while True:
        print("\n" + "-" * 40)
        print("              MAIN MENU")
        print("-" * 40)
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Display Account Information")
        print("5. Exit")
        print("-" * 40)
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == "1":
                # Deposit
                amount = get_valid_amount("Enter deposit amount: ₱")
                try:
                    new_balance = account.deposit(amount)
                    print(f"New balance: ₱{new_balance:.2f}")
                except ValueError as e:
                    print(f"Deposit failed: {e}")
            
            elif choice == "2":
                # Withdraw
                amount = get_valid_amount("Enter withdrawal amount: ₱")
                try:
                    new_balance = account.withdraw(amount)
                    print(f"New balance: ₱{new_balance:.2f}")
                except ValueError as e:
                    print(f"Withdrawal failed: {e}")
            
            elif choice == "3":
                # Check Balance
                print(f"\nCurrent Balance: ₱{account.get_balance():.2f}")
            
            elif choice == "4":
                # Display Account Information
                account.display_account_info()
            
            elif choice == "5":
                # Exit
                print("\nThank you for using the Bank Account Management System!")
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
