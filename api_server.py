# api_server.py
import json
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)
DB_FILE = 'employees.json'

def read_db():
    """Reads the entire database from the JSON file."""
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"employees": []}

def write_db(data):
    """Writes data to the JSON file."""
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/employees', methods=['GET'])
def get_employees():
    """Endpoint to fetch all employees."""
    print("GET request received for /employees")
    data = read_db()
    return jsonify(data['employees'])

@app.route('/employee/update', methods=['POST'])
def update_employee():
    """Endpoint to update an employee's salary."""
    update_data = request.get_json()
    emp_id = update_data.get('id')
    new_salary = update_data.get('salary')
    
    if not emp_id or new_salary is None:
        return jsonify({"status": "error", "message": "Missing id or salary"}), 400

    print(f"POST request received to update employee {emp_id} with new salary {new_salary}")
    
    db_data = read_db()
    employee_found = False
    for emp in db_data['employees']:
        if emp['id'] == emp_id:
            emp['salary'] = new_salary
            employee_found = True
            break
    
    if employee_found:
        write_db(db_data)
        return jsonify({"status": "success", "message": f"Employee {emp_id} updated."})
    else:
        return jsonify({"status": "error", "message": f"Employee {emp_id} not found."}), 404

if __name__ == '__main__':
    # Running on http://127.0.0.1:5000
    app.run(debug=True)