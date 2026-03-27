import pandas as pd

data = {
    'carat':[0.23,0.21,0.23,0.29,0.31],
    'cut':['Ideal','Premium','Good','Premium','Good'],
    'color':['E','E','E','I','J'],
    'clarity':['SI2','SI1','VS1','VS2','SI2'],
    'depth':[61.5,59.8,56.9,62.4,63.3],
    'table':[55.0,61.0,65.0,58.0,58.0],
    'price':[326,326,327,334,335],
    'x':[3.95,3.89,4.05,4.20,4.34],
    'y':[3.98,3.84,4.07,4.23,4.35],
    'z':[2.43,2.31,2.31,2.63,2.75]
}

df = pd.DataFrame(data)

mean_price = df.groupby('cut')['price'].mean()
print(mean_price)

count = df.groupby('cut')['price'].count()
min_price = df.groupby('cut')['price'].min()
max_price = df.groupby('cut')['price'].max()

print(count)
print(min_price)
print(max_price)

avg_x = df['x'].mean()
avg_y = df['y'].mean()
avg_z = df['z'].mean()

print(avg_x, avg_y, avg_z)

df2 = pd.read_excel('employee.xlsx')

auto_emp = df2[df2['Department'] == 'Automotive']
print(auto_emp)

emp_id = int(input())
emp_details = df2[df2['Employee ID'] == emp_id]
print(emp_details)

developers = df2[df2['Designation'] == 'Developer']
print(developers)