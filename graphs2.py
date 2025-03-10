from matplotlib import pyplot as plt
import pandas as pd
import pymysql
# Connect to MySQL database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="finaldb",
    port=3333
)
'''
#1.Show skill wise highest salary?
query = "SELECT Empskill , max(Empsalary) AS MaxSalary FROM finalemp GROUP BY Empcompany;"
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
# Plot the data bar
plt.bar(df['Empskill'], df['MaxSalary'], color=['pink','green'])
plt.xlabel('Empskill')
plt.ylabel('Max Salary')
plt.title('Show skill wise highest salary')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.show()
#2 Show company wise least salary.?
# Read data from MySQL table into a DataFrame
query = "SELECT Empcompany, min(Empsalary) AS MinSalary FROM finalemp GROUP BY Empcompany;"
df = pd.read_sql(query,connection)
# Close the connection
connection.close()
# Plot the data bar
plt.scatter(df['Empcompany'], df['MinSalary'], color='yellow')
plt.xlabel('Empcompany')
plt.ylabel('Min Salary')
plt.title('Minimum Salary by Empcompany')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
                      # Add grid lines for better visualization
plt.show()

#pie
plt.pie(df['MinSalary'], labels=df['Empcompany'], autopct='%1.1f%%', startangle=140)
plt.title('Minimum Salary Distribution by Company (Pie Chart)')
# Area plot
plt.fill_between(df['Empcompany'],df['MinSalary'],color='pink')
plt.xlabel('Empompany')
plt.ylabel('Min Salary')
plt.show()
import matplotlib.pyplot as plt
# Line plot
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.plot(df['Empcompany'], df['MinSalary'], marker='o', color='blue', linestyle='-')
plt.xlabel('Empompany')
plt.ylabel('Min Salary')
plt.title('Minimum Salary by Company')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['MinSalary'], bins=10, color='green')
plt.xlabel('Minimum Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Minimum Salary')
plt.grid(True)
plt.show()
#3.Show company_location wise count of employees
query='select Emplocation,count(*) as CountofEmployees from finalemp GROUP BY Emplocation;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()

plt.bar(df['Emplocation'],df['CountofEmployees'],color='red',width=0.3)
plt.xlabel('Emplocation')
plt.ylabel('Count of Employees')
plt.title('Company Locationwise CountOfEmloyees')
plt.show()
#4.Show qualification wise latest passedoutyear
query="SELECT Empqualification,Emppassedoutyear from finalemp GROUP BY Empqualification ORDER BY Emppassedoutyear DESC;"
df = pd.read_sql(query, connection)
#close the connection
connection.close()
plt.bar(df['Empqualification'],df['Emppassedoutyear'],color='yellow')
plt.xlabel('Empqualification')
plt.ylabel('Emppassedoutyear')
plt.title('Qualification wise Latest passedoutyear')
plt.show()

#5.Show gender wise highest salary
query='select Empgender,max(Empsalary ) as  Maxsalary  from finalemp GROUP BY Empsalary;'
df = pd.read_sql(query, connection)
#close the connection
connection.close()
plt.bar(df['Empgender'],df['Maxsalary'],color='green',width=0.1)
plt.xlabel('Empgender')
plt.ylabel('Maxsalary')
plt.title('Gender wise highest salary')
plt.show()
#6.Show gender wise count of employees?
query='select Empgender,count(*) as CountofEmployees from finalemp GROUP BY Emplocation;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empgender'],df['CountofEmployees'],color='yellow',width=0.15)
plt.xlabel('Gender')
plt.ylabel('Count Of Employees')
plt.title('Gender wise Count of employees')
plt.show()
#7.Show highest wise sum of salary?
query='select Empheight,sum(Empsalary) as Sumofsalary from finalemp GROUP BY Empheight;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empheight'],df['Sumofsalary'],color='blue',width=0.3)
plt.xlabel('Height Of Employee')
plt.ylabel('Sum of Salary')
plt.title('Show highest wise sum of salary')
plt.show()
#8.Show passedoutyear year count of employees.?
query='select Emppassedoutyear,count(*) as CountOfEmployees from finalemp GROUP BY Empheight;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Emppassedoutyear'],df['CountOfEmployees'],color='pink')
plt.xlabel('PassedOutYear')
plt.ylabel('Count of Employees')
plt.title('Passedoutyear Wise Count of employees.')
plt.grid(True)
plt.show()
#9.Show qualification wise highest monthly_expenses?
query='select Empqualification,max( Empmothly_expenses) as Expenses from finalemp GROUP BY  Empqualification;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empqualification'],df['Expenses'],color='blue')
plt.xlabel('Qualification')
plt.ylabel('Expenses')
plt.title('Qualification wise highest monthly_expenses')
plt.show()
#10.Show hometown wise count of employees
query='select  Emphometown,count(* ) as CountOfEmployees from finalemp GROUP BY Emphometown;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Emphometown'],df['CountOfEmployees'],color='brown',width=0.50)
plt.xlabel('Hometown')
plt.ylabel('CountOfEmployees')
plt.title('Employee Hometown wise count of employees')
plt.show()
#11.Show skill wise highest bonus
query='select Empskill ,max(Empbonus) as Bonus from finalemp GROUP BY  Empskill;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empskill'], df['Bonus'], color='green')
plt.xlabel('Skill')
plt.ylabel('Bonus')
plt.title('Show skill wise highest bonus')
plt.show()

#12.Show skill wise highest exp of employee
query='select Empskill ,max(Empexperience) as Experiance from finalemp GROUP BY  Empskill;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.pie(df['Experiance'], labels=df['Empskill'], autopct='%1.1f%%', startangle=140)
plt.title('Skill wise highest exp of employee')
plt.show()
#13.Show gender wise young employee age
query='select  Empgender ,min(Empage) as age from finalemp GROUP BY Empgender;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empgender'], df['age'], color='green',width=0.3)
plt.xlabel('Empgender ')
plt.ylabel('Empage')
plt.title('Gender wise young employee age')
plt.show()

#14.Show gender wise sum of bonus?
query='select  Empgender ,sum(Empbonus) as Bonus from finalemp GROUP BY Empgender;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empgender'], df['Bonus'], color='orange',width=0.3)
plt.xlabel('Gender ')
plt.ylabel('Bonus')
plt.title('Show gender wise sum of bonus')
plt.show()

#15.Show age wise highest salary?
query='select  Empage, max(Empsalary) as Salary from finalemp GROUP BY Empage;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()

plt.bar(df['Empage'], df['Salary'], color='yellow',width=3.5)
plt.xlabel('age')
plt.ylabel('salary')
plt.title('Show age wise highest salary')
plt.show()
plt.pie(df['Salary'], labels=df['Empage'], autopct='%1.5f%%', startangle=200)
plt.title('Show skill wise highest exp of employee')
plt.show()
#16.Show count of employees who is having ownCar.
query='select  EmpownCar, Count(*) as countOfEmployees from finalemp GROUP BY  Empowncar;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['EmpownCar'], df['countOfEmployees'], color='blue',width=0.3)
plt.xlabel('OwnCar')
plt.ylabel('countOfEmployee')
plt.title('Count of Employees with OwnCar')
plt.show()
#17.Show count of employees who is having ownHouse.
query='select   Empownhouse, Count(*) as countofemployees from finalemp GROUP BY   Empownhouse;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.scatter(df['Empownhouse'], df['countofemployees'], color='black')
plt.xlabel('OwnHouse')
plt.ylabel('countofemployees')
plt.title('Count of employees who is having ownHouse.')
plt.grid(True)
plt.show()
#18.Show sum of bonus of employees who is having ownCar?
query='select   Empowncar, sum(Empbonus) as  bonus from finalemp GROUP BY Empowncar;'
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empowncar'], df['bonus'], color='blue',width=0.3)
plt.xlabel('OwnCar')
plt.ylabel('Count')
plt.title('sum of bonus of employees who is having ownCar')
plt.show()
#19.Show the highest salary of employees who is having ownCar and not having ownCar?
query = 'SELECT Empowncar, max(Empsalary) AS Maxsalary FROM finalemp GROUP BY Empowncar;'
# Read data into a DataFrame
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
# Plotting
plt.scatter(df['Empowncar'], df['Maxsalary'], color=['blue','pink'])
plt.xlabel('OwnCar')
plt.ylabel('Highest Salary')
plt.title('Highest Salary of Employees based on Car Ownership')
plt.xticks(ticks=[0, 1], labels=['Not OwnCar', 'OwnCar'])
plt.grid(True)
plt.show()
#20.Show the sum of salary of employees who is having ownHouse and not having ownHouse?
query = 'SELECT  Empownhouse, SUM(Empsalary) AS salary FROM finalemp GROUP BY  Empownhouse;'
# Read data into a DataFrame
df = pd.read_sql(query, connection)
# Close the connection
connection.close()
plt.bar(df['Empownhouse'], df['salary'], color=['orange', 'green'],width=0.3)
plt.xlabel('OwnHouse')
plt.ylabel('Highest Salary')
plt.title('Highest Salary of Employees based on OwnHouse')
plt.xticks(ticks=[0, 1], labels=['Not OwnHouse', 'OwnHouse'])
plt.show()

