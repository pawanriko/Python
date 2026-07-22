name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
college = input("Enter your college name: ")
print("\n=== User Information ===")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"City    : {city}")
print(f"College : {college}")

english = int(input("Enter your English marks: "))
maths = int(input("Enter your Maths marks: "))
science = int(input("Enter your Science marks: "))
total_marks = english + maths + science
number_of_subjects = 3
average = total_marks / number_of_subjects
print("\n=== Marks Information ===")
print(f"English Marks : {english}")
print(f"Maths Marks   : {maths}")
print(f"Science Marks : {science}")
print(f"Total Marks   : {total_marks}")
print(f"Average Marks : {average:.2f}")

employee_name = input("Enter employee name: ")
employee_salary = float(input("Enter employee salary: "))
annual_salary = employee_salary * 12
print("\n=== Employee Information ===")
print(f"Employee Name   : {employee_name}")
print(f"Employee Salary : {employee_salary:.2f}")
print(f"Annual Salary   : {annual_salary:.2f}")