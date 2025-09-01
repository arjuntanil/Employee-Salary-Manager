# Employee Salary Manager 💼

A simple Python application to demonstrate a client-server architecture for managing employee salaries. This project uses a local Flask API to serve data and a separate client script to fetch, process, and update employee information, showcasing modularity, object-oriented principles, and real-world API communication.

---

## ✨ Core Features

* **Modular Design:** Code is logically separated into an API server, a client, utility functions, and an employee class.
* **Object-Oriented Programming (OOP):** Utilizes an `Employee` class to structure and manage employee data cleanly.
* **Client-Server Architecture:** A Flask server (`api_server.py`) acts as the backend, and a client script (`main.py`) consumes its API.
* **Local API Simulation:** Demonstrates `GET` and `POST` requests using the `requests` library to interact with the server.
* **Virtual Environment Ready:** All dependencies are managed in `requirements.txt` for easy and reproducible setup.

---

## 📁 Project Structure

employee_salary_manager/
│
├── venv/
├── api_server.py       # The Flask API server
├── main.py             # The main client application
├── employee_module.py  # Contains the Employee class definition
├── salary_utils.py     # Utility functions for making API calls
├── employees.json      # The JSON file acting as a simple database
├── .gitignore          # Specifies files for Git to ignore
└── requirements.txt    # Project dependencies

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

* Python 3.8+
* Git

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/arjuntanil/Employee-Salary-Manager.git](https://github.com/arjuntanil/Employee-Salary-Manager.git)
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run

This project requires two terminals running simultaneously: one for the server and one for the client.

### 1. In Terminal 1: Start the API Server

This terminal will run the Flask server that listens for requests.

```bash
python api_server.py
```


You should see output indicating the server is running, like this:

 * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
Leave this terminal running.

### 2. In Terminal 2: Run the Client Application
This terminal will run the main script that fetches data, applies bonuses, and sends updates back to the server.


```bash
python main.py
```

The client will execute the process and print the final report to the console:

### Employee Salary Manager 

Fetching employee data from the local API...
Found 3 employees.

### Applying Bonuses and Generating Report 
Alice      | Final Salary: 33000.0
Bob        | Final Salary: 35200.0
Charlie    | Final Salary: 38500.0

### Sending Updates to the API
Successfully updated salary for Alice. Status: success
Successfully updated salary for Bob. Status: success
Successfully updated salary for Charlie. Status: success

### Process Complete
🛠️ How It Works
The application operates on a simple client-server model:

The api_server.py script acts as the backend. It reads from and writes to the employees.json file and exposes two endpoints:

 * GET /employees: To provide a list of all employees.
 * POST /employee/update: To update the salary of a specific employee.
 * The main.py script is the client. It performs the following sequence of operations:
 * It calls fetch_employees() to make a GET request to the server to get the employee data.
 * It processes this data locally, applying a bonus to each employee's salary.
 * It prints a formatted report to the console.
 * Finally, it calls post_salary_update() in a loop to send a POST request for each employee, telling the server to save the new salary.
