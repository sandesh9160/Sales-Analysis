import pymysql

def export_data_to_text_file(host, user, password, database, table, output_file):
    try:
        # Connect to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='textdb',
            port=3333
        )

        with connection.cursor() as cursor:
            # Query to fetch data from the specified table
            query = f"SELECT * FROM {table}"

            # Execute the query
            cursor.execute(query)

            # Fetch all rows
            rows = cursor.fetchall()

            # Write the fetched data to the text file
            with open(output_file, 'w') as file:
                for row in rows:
                    # Convert each row to a string and write it to the file
                    row_str = ','.join(str(cell) for cell in row)
                    file.write(row_str + '\n')

            print(f"Data exported to {output_file}")

    except pymysql.Error as error:
        print("Error connecting to MySQL database:", error)

    finally:
        if connection.open:
            connection.close()
            print("MySQL connection is closed")

# Example usage
export_data_to_text_file(
    host='localhost',
    user='root',
    password='root',
    database='textdb',
    table='textapp_textdb;',
    output_file='textdata.txt'
)
