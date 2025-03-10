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
try:
    plt.figure(figsize=(21, 14))  # Adjust figure size
    for i in range(1, 11):
        plt.subplot(3, 4, i)  # Create subplot grid with 3 rows and 4 columns
        if i == 1:
            #1. Plot for skill wise highest salary
            query = "SELECT Empskill, MAX(Empsalary) AS Salary FROM finalemp GROUP BY Empskill;"
            df_skill_salary = pd.read_sql(query, connection)
            plt.plot(df_skill_salary['Empskill'], df_skill_salary['Salary'], color='green')
            plt.xlabel('Empskill')
            plt.ylabel('Highest Salary')
            plt.title('Skill wise Highest Salary')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        elif i == 2:
            #2. Show company wise least salary
            query = "SELECT Empcompany, min(Empsalary) AS MinSalary FROM finalemp GROUP BY Empcompany;"
            df = pd.read_sql(query, connection)
            plt.scatter(df['Empcompany'], df['MinSalary'], color='green')
            plt.xlabel('EmpCompany')
            plt.ylabel('Min Salary')
            plt.title('Company wise Least Salary')
        

        elif i == 3:
            #3. Plot for company location count
            query = "SELECT Emplocation, COUNT(*) AS CountofEmployees FROM finalemp GROUP BY Emplocation;"
            df_location_count = pd.read_sql(query, connection)
            plt.bar(df_location_count['Emplocation'], df_location_count['CountofEmployees'], color='red')
            plt.xlabel('EmployeeLocation')
            plt.ylabel('CountofEmployee')
            plt.title('Company Location Wise CountOfEmployees')
            plt.xticks(rotation=45)
            

        elif i == 4:
            # 4. Show qualification wise latest passedoutyear
            query = "SELECT Empqualification, Emppassedoutyear FROM finalemp GROUP BY Empqualification ORDER BY Emppassedoutyear;"
            df = pd.read_sql(query, connection)
            plt.pie(df['Emppassedoutyear'], labels=df['Empqualification'], autopct='%1.1f%%', startangle=140)
            plt.xlabel('Qualification')
            plt.title('Qualification wise Latest Passed Out Year')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        elif i == 5:
            #5. Show gender wise highest salary
            query = "SELECT Empgender, MAX(Empsalary) AS HighestSalary FROM finalemp GROUP BY Empgender;"
            df = pd.read_sql(query, connection)
            plt.scatter(df['Empgender'], df['HighestSalary'])
            plt.xlabel('Gender')
            plt.ylabel('Salary')
            plt.title('Gender wise Highest Salary')
            plt.grid(True)

        elif i == 6:
            #6. Show gender wise count of employees
            query = "SELECT Empgender, COUNT(*) AS Count FROM finalemp GROUP BY Empgender;"
            df = pd.read_sql(query, connection)
            plt.pie(df['Count'], labels=df['Empgender'], startangle=140)
            plt.xlabel('Gender')
            plt.title('Gender wise Count of Employees')

        elif i == 7:
            #7. Show height wise sum of salary
            query = "SELECT Empheight, SUM(Empsalary) AS TotalSalary FROM finalemp GROUP BY Empheight;"
            df = pd.read_sql(query, connection)
            plt.plot(df['Empheight'], df['TotalSalary'], color='blue')
            plt.xlabel('Height')
            plt.ylabel('Total Salary')
            plt.title('Height wise Total Salary')

        elif i == 8:
            #8. Show passed out year count of employees
            query = "SELECT Emppassedoutyear, COUNT(*) AS CountOfEmployees FROM finalemp GROUP BY Emppassedoutyear;"
            df = pd.read_sql(query, connection)
            plt.hist(df['Emppassedoutyear'], bins=10, color='purple')
            plt.xlabel('Emppassedoutyear')
            plt.ylabel('CountOfEmployees')
            plt.title('Passed Out Year Count of Employees')

        elif i == 9:
            #9. Show qualification wise highest monthly expenses
            query = "SELECT Empqualification, MAX(Empmothly_expenses) AS HighestExpenses FROM finalemp GROUP BY Empqualification;"
            df = pd.read_sql(query, connection)
            plt.bar(df['Empqualification'], df['HighestExpenses'], color='skyblue')
            plt.xlabel('Qualification')
            plt.ylabel('Highest Monthly Expenses')
            plt.title('Qualification wise Highest Monthly Expenses')

        elif i == 10:
            #10. Show hometown wise count of employees
            query = "SELECT Emphometown, COUNT(*) AS CountofEmployees FROM finalemp GROUP BY Emphometown;"
            df = pd.read_sql(query, connection)
            plt.violinplot(df['CountofEmployees'], vert=False)
            plt.yticks([1], ['CountofEmployees'])
            plt.xlabel('CountofEmployees')
            plt.title('Hometown wise Count of Employees  else')
            # Additional plots can be added here similarly
            pass

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the connection
    connection.close()
