1. Problem Statement
The program manages employee details such as employee ID, name, role, and salary. It reads employee records from a text file and displays their details. It also identifies employees earning above ₹50,000, finds the highest-paid employee, and counts the number of employees in each role.

2. Progarm/Logic used

Step 1: Create Employee Class
The employee class is created to store employee details such as ID, name, role, and salary.

Step 2: Read Employee Details
The read_employee() function reads employee records from the employees.txt file and stores them in a list of employee objects.

Step 3: Add Employee Details
The add_employee() function adds new employee details to the text file.

Step 4: Display Employee Details
The display_details() function displays each employee's ID, name, role, and salary.

Step 5: Find Employees Earning Above ₹50,000
The program checks employee salaries and displays the names and salaries of employees earning more than ₹50,000.

Step 6: Find the Highest-Paid Employee
The find_highest_salary() function uses the max() function and a lambda expression to identify the employee with the highest salary.

Step 7: Count Employees by Role
The rolecount() function counts the number of employees in each role using a dictionary.

3. How to Run the Program
Save the Python code in a file named main.py.
Create an employees.txt file in the same folder as the Python program.
Add employee records to the text file in the following format:
101,Carline,Python Developer,50000
102,Prisilla,Tester,45000
103,John,Developer,60000
104,Priya,Tester, 48000
Run the Python program in the terminal.
View the employee details, employees earning above ₹50,000, the highest-paid employee, and the employee count by role.

4. Sample Input
The following records are stored in employees.txt:
101,Carline,Python Developer,50000
102,Prisilla,Tester,45000
103,John,Developer,60000
104,Priya,Tester, 48000

5. Sample Output

-----Employee Details-----
101- Carline- Python Developer- ₹50000
102- Prisilla- Tester- ₹45000
103- John- Developer- ₹60000
104- Priya- Tester- ₹48000
-----Employee with salary>5000-----
John - ₹60000
The highest paid employee: John - ₹60000
Developer - 1
Python Developer - 1
Tester - 2

6. Concepts Used
Classes and Objects: Represent employee records as objects.
Constructor (__init__()): Initializes employee attributes.
Instance Methods: Display individual employee details.
Static Methods: Perform operations such as reading employee data, adding employees, finding the highest salary, and counting roles.
File Handling: Read from and append data to employees.txt.
Exception Handling: Handle missing files using try and except.
Lists: Store employee objects.
Dictionaries: Count employees by role.
List Iteration: Process employee records using for loops.
Conditional Statements: Filter employees based on salary.
Lambda Functions: Select the employee with the highest salary.
Built-in Functions: Use max(), sorted(), and int().
String Methods: Use strip() and split() to process file data