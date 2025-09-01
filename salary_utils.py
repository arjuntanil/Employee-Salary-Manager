# salary_utils.py
import requests
from employee_module import Employee

API_BASE_URL = "http://127.0.0.1:5000"

def fetch_employees():
    """
    Fetches all employees from the local API.
    
    Returns:
        list: A list of Employee objects, or an empty list on failure.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/employees")
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
        employees_data = response.json()
        
        # Convert raw dictionary data into Employee objects
        return [Employee(e['id'], e['name'], e['salary']) for e in employees_data]
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employees: {e}")
        return []

def post_salary_update(employee):
    """
    Sends a POST request to update an employee's salary.
    
    Args:
        employee (Employee): The employee object with updated data.
    """
    try:
        payload = {
            "id": employee.emp_id,
            "salary": employee.salary + employee.bonus # Send the final salary
        }
        response = requests.post(f"{API_BASE_URL}/employee/update", json=payload)
        response.raise_for_status()
        print(f"Successfully updated salary for {employee.name}. Status: {response.json()['status']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error updating salary for {employee.name}: {e}")