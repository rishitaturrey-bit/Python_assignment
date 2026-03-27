import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('sales_data.csv')

plt.figure()
plt.plot(data['month_number'], data['total_profit'])
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Total Profit per Month')
plt.show()

plt.figure()
plt.plot(data['month_number'], data['facecream'], label='Face Cream')
plt.plot(data['month_number'], data['facewash'], label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Product Sales Data')
plt.show()

plt.figure()
plt.bar(data['month_number'], data['facecream'], label='Face Cream')
plt.bar(data['month_number'], data['facewash'], bottom=data['facecream'], label='Face Wash')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream and Face Wash Sales')
plt.legend()
plt.show()

total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title('Total Sales per Product')
plt.show()

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'Atos', 'Amdocs']
recruitments = [120, 150, 180, 100, 90, 110, 70, 80]

plt.figure()
plt.bar(companies, recruitments)
plt.xticks(rotation=30)
plt.title('New Recruitments')
plt.show()

plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title('Recruitment Share')
plt.show()

explode = [0, 0.1, 0, 0, 0, 0, 0, 0]
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title('Customized Pie Chart')
plt.show()

plt.figure()
plt.pie(recruitments, labels=companies, wedgeprops={'width':0.4})
plt.title('Doughnut Chart')
plt.show()

ibm_amdocs = ['IBM', 'Amdocs']
values = [100, 80]

plt.figure()
plt.bar(ibm_amdocs, values)
plt.title('IBM vs Amdocs Recruitment')
plt.show()