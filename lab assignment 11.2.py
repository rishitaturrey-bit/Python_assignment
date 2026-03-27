import matplotlib.pyplot as plt

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