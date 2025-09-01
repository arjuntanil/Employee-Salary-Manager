# main.py
from salary_utils import fetch_employees, post_salary_update

# --- Configuration ---
BONUS_PERCENTAGE = 10.0 # Define the bonus percentage here

def main():
    """Main function to run the employee salary management process."""
    print("--- Employee Salary Manager ---")
    
    # 1. Fetch employees from the API
    print(f"\nFetching employee data from the local API...")
    employees = fetch_employees()
    
    if not employees:
        print("Could not retrieve employee data. Exiting.")
        return
        
    print(f"Found {len(employees)} employees.")
    
    print("\n--- Applying Bonuses and Generating Report ---")
    
    # 2. Iterate over employees to apply bonus and print report
    for emp in employees:
        # Apply the bonus
        final_salary = emp.apply_bonus(BONUS_PERCENTAGE)
        
        # Print the report for this employee
        print(emp) # This uses the __str__ method from the Employee class
    
    print("\n--- Sending Updates to the API ---")

    # 3. Iterate again to send POST requests with updates
    for emp in employees:
        post_salary_update(emp)
        
    print("\n--- Process Complete ---")

if __name__ == '__main__':
    main()