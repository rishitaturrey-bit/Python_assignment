import pandas as pd

df = pd.read_excel(r"C:\Users\Rishita\PycharmProjects\Python_assignment\employee.xlsx",engine="openpyxl")

auto_emp = df[df['Department'] == 'Automotive']
print(auto_emp)

emp_id = int(input())
emp_details = df[df['Employee ID'] == emp_id]
print(emp_details)

developers = df[df['Designation'] == 'Developer']
print(developers)