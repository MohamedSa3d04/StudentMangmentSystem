# Student Management System

This is a simple Student Management System implemented in Python using the Tkinter library for the graphical user interface and MySQL for the backend database. The system allows you to manage student information, such as adding, deleting, updating, and searching for student records.

## Prerequisites
- Python installed on your machine (https://www.python.org/)
- MySQL installed on your machine (https://www.mysql.com/)

## Installation
1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/Student-Management-System.git
cd StudentManagementSystem
```

2. Install the required Python packages.

```bash
pip install pymysql
```

3. Import the provided SQL script (`student.sql`) into your MySQL database to create the necessary table.

4. Update the MySQL connection details in the code.

```python
# Inside the code (StudentManagementSystem.py), update the following lines with your MySQL connection details.
con = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='student'
)
```

## How to Run
Run the main script `StudentManagementSystem.py` to launch the application.

```bash
python StudentManagementSystem.py
```

## Features
- Add new student records.
- Delete student records by ID.
- Update student information.
- Search for students by ID or name.
- View a table of all student records.

## Usage
1. Launch the application using the command mentioned above.
2. Fill in the student information in the provided fields.
3. Use the buttons to perform different operations (Add Student, Delete Student, Update Student, Clear Fields, Exit).
4. You can search for students by specifying the search criteria (ID or Name) and entering the corresponding value.
5. The student records are displayed in a table, and you can click on a row to fill the fields with the selected student's information.

Feel free to use, modify, and enhance the code according to your needs. If you encounter any issues or have suggestions for improvement, please create an issue in the repository.

## Author
Eng/Mohamed Saad
