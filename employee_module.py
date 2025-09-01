# employee_module.py

class Employee:
    """A class to represent an employee."""
    
    def __init__(self, emp_id, name, salary):
        """Initializes the Employee object."""
        self.emp_id = emp_id
        self.name = name
        self.salary = float(salary)
        self.bonus = 0.0

    def apply_bonus(self, percentage):
        """
        Applies a bonus to the employee's salary.
        
        Args:
            percentage (float): The bonus percentage (e.g., 10 for 10%).
            
        Returns:
            float: The final salary including the bonus.
        """
        self.bonus = self.salary * (percentage / 100)
        final_salary = self.salary + self.bonus
        return final_salary
    
    def __str__(self):
        """String representation for printing the report."""
        final_salary = self.salary + self.bonus
        return f"{self.name:<10} | Final Salary: {final_salary}"