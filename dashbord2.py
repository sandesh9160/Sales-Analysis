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
            # Plot for skill wise highest salary
            query = "SELECT Empskill, MAX(Empbonus) AS Bonus FROM finalemp GROUP BY Empskill;"
            df = pd.read_sql(query, connection)
            plt.plot(df['Empskill'], df['Bonus'], color='blue')
            plt.xlabel('Skill')
            plt.ylabel('Bonus')
            plt.title('Show skill wise highest bonus')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        elif i == 2:
            # Show Experience Wise Skill
            query = "SELECT Empskill, MAX(Empexperience) AS Experience FROM finalemp GROUP BY Empskill;"
            df = pd.read_sql(query, connection)
            plt.scatter(df['Empskill'], df['Experience'], color='black')
            plt.xlabel('Empskill')
            plt.ylabel('Experience')
            plt.title('Experience Wise Skill')
            plt.grid(True)

        elif i == 3:
            # Show gender wise young employee age
            query = "SELECT Empgender, MIN(Empage) AS age FROM finalemp GROUP BY Empgender;"
            df = pd.read_sql(query, connection)
            plt.bar(df['Empgender'], df['age'], color=['yellow','blue'],width=0.15)
            plt.xlabel('Empgender')
            plt.ylabel('Age')
            plt.title('Gender wise young employee age')
            plt.xticks(rotation=45)

        elif i == 4:
            # Show gender wise sum of bonus
            query = "SELECT Empgender, SUM(Empbonus) AS Bonus FROM finalemp GROUP BY Empgender;"
            df = pd.read_sql(query, connection)
            plt.pie(df['Bonus'], labels=df['Empgender'], autopct='%1.1f%%', startangle=140)
            plt.xlabel('Empgender')
            plt.title('Gender wise sum of bonus')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        elif i == 5:
            # Show age wise highest salary
            query = "SELECT Empage, MAX(Empsalary) AS MaxSalary FROM finalemp GROUP BY Empage;"
            df = pd.read_sql(query, connection)
            plt.scatter(df['Empage'], df['MaxSalary'])
            plt.xlabel('Empage')
            plt.ylabel('MaxSalary')
            plt.title('Age wise Highest Salary')
            plt.grid(True)

        elif i == 6:
            # Show count of employees who are having ownCar
            query = "SELECT EmpownCar, COUNT(*) AS countOfEmployees FROM finalemp GROUP BY EmpownCar;"
            df = pd.read_sql(query, connection)
            plt.hist(df['countOfEmployees'])
            plt.title('Count of employees who are having ownCar')

        elif i == 7:
            # Show count of employees who are having ownHouse
            query = "SELECT Empownhouse, COUNT(*) AS countofemployees FROM finalemp GROUP BY Empownhouse;"
            df = pd.read_sql(query, connection)
            plt.plot(df['Empownhouse'], df['countofemployees'], color='blue')
            plt.xlabel('Empownhouse')
            plt.ylabel('countofemployees')
            plt.title('Count of employees who are having ownHouse')

        elif i == 8:
            # Show sum of bonus of employees who are having ownCar
            query = "SELECT Empowncar, SUM(Empbonus) AS bonus FROM finalemp GROUP BY Empowncar;"
            df = pd.read_sql(query, connection)
            plt.bar(df['Empowncar'], df['bonus'], color='orange')
            plt.xlabel('Empowncar')
            plt.ylabel('bonus')
            plt.title('Sum of bonus of employees who are having ownCar')

        elif i == 9:
            # Show the highest salary of employees who are having ownCar and not having ownCar
            query = "SELECT Empowncar, MAX(Empsalary) AS Maxsalary FROM finalemp GROUP BY Empowncar;"
            df = pd.read_sql(query, connection)
            plt.plot(df['Empowncar'], df['Maxsalary'], color='blue')
            plt.xlabel('Empowncar')
            plt.ylabel('Maxsalary')
            plt.title('Highest salary of employees who are having ownCar and not having ownCar')
            plt.legend()

        elif i == 10:
            # Show hometown wise sum of salaries
            query = "SELECT Empownhouse, SUM(Empsalary) AS salary FROM finalemp GROUP BY Empownhouse;"
            df = pd.read_sql(query, connection)
            plt.bar(df['Empownhouse'], df['salary'], color=['black','red'],width=0.5)
            plt.xlabel('Empownhouse')
            plt.ylabel('Salary')
            plt.title('Hometown wise sum of salaries')

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the connection
    connection.close()
