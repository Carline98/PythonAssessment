1. Problem Statement
The program collects student details and marks in Python, SQL, and AI. It calculates the total and average marks, assigns grades, and determines whether each student has passed or failed. It also identifies the highest-scoring student and displays the names of students whose average marks are above 75.

2. Approach/Logic Used

The program follows these steps:
Step 1: Define Grade Function
The grade(avg) function assigns a grade (A, B, C, D, or F) based on the student's average marks.

Step 2: Define Result Function
The result(avg) function determines whether the student passes or fails based on their average marks.

Step 3: Collect Student Details
The program asks for the number of students and collects the following details for each student:
Student ID
Student name
Python marks
SQL marks
AI marks

Step 4: Calculate Total and Average
The total marks are calculated by adding the marks obtained in all three subjects.
Formula:
Total = Python Marks + SQL Marks + AI Marks
Average = Total / 3

Step 5: Store Student Records
Each student's information, total, average, grade, and result are stored in a dictionary. All student dictionaries are added to the Students list.

Step 6: Display Student Details
The program iterates through the list and displays each student's ID, name, total marks, average, grade, and result.

Step 7: Find the Highest-Scoring Student
The max() function with a lambda expression identifies the student with the highest average marks.

Step 8: Find Students Scoring Above 75
A list comprehension filters and displays the names of students whose average marks are strictly greater than 75. Students with an average of exactly 75 are not included.

3. How to Run the Program

Open the main.py file in your code editor.
Run the following command in the terminal:
python main.py
Enter the number of students.
Enter each student's ID, name, and marks when prompted.
View the student records, highest-scoring student, and list of students scoring above 75

4. Sample Input
-----Student Details-----
The Number of Students: 2
Student ID: 101
Name of the Student: carline
Python Marks: 45
SQL Marks: 67
AI Marks: 66

Student ID: 102
Name of the Student: prisilla
Python Marks: 88
SQL Marks: 69
AI Marks: 97

5. Sample Output

Student ID: 101
Name of the Student: carline
Total of the Student: 178.000000
Average of the Student: 59.33
Grade of the student: C
Result of the student: PASS

Student ID: 102
Name of the Student: prisilla
Total of the Student: 254.000000
Average of the Student: 84.67
Grade of the student: B
Result of the student: PASS

Highest Scoring Student: prisilla
Student Scoring above 75: prisilla

6. python concepts used
Functions: Used to calculate grades and pass/fail results.
Conditional Statements: Used to assign grades and determine results based on average marks.
Input and Output: Used to accept student details and display results.
Type Conversion: Used int() to convert input into integers.
Lists: Used to store multiple student records.
Dictionaries: Used to store each student's details and marks.
For Loops: Used to collect and display student information.
Arithmetic Operators: Used to calculate total and average marks.
Built-in Functions: Used max() to find the highest-scoring student.
Lambda Function: Used to compare students based on their average marks.
List Comprehension: Used to find students scoring above 75.
String Formatting: Used f-strings to display student details neatly.
String Method: Used join() to display student names separated by commas