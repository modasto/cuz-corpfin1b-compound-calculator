import math

def get_valid_float(prompt):
    """Ensures the user provides a valid numeric input."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number (e.g., 500 or 0.05).")

def calculate_fv():
    """Computes Future Value: FV = PV * e^(rt)"""
    print("\n--- Calculating Future Value ---")
    pv = get_valid_float("Enter Present Value (PV): ")
    r = get_valid_float("Enter annual interest rate (as decimal, e.g., 0.05): ")
    t = get_valid_float("Enter time in years (t): ")
    
    fv = pv * math.exp(r * t)
    print(f"\nResult: The Future Value is ${fv:,.2f}")

def calculate_pv():
    """Computes Present Value: PV = FV / e^(rt)"""
    print("\n--- Calculating Present Value ---")
    fv = get_valid_float("Enter Future Value (FV): ")
    r = get_valid_float("Enter annual interest rate (as decimal, e.g., 0.05): ")
    t = get_valid_float("Enter time in years (t): ")
    
    pv = fv / math.exp(r * t)
    print(f"\nResult: The Present Value is ${pv:,.2f}")

def main():
    while True:
        print("\n================================")
        print(" CONTINUOUS COMPOUNDING CALCULATOR")
        print("================================")
        print("1. Calculate Future Value (FV)")
        print("2. Calculate Present Value (PV)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            calculate_fv()
        elif choice == '2':
            calculate_pv()
        elif choice == '3':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
