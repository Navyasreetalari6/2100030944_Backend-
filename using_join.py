import mysql.connector

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Navya123",
        database="Navya"
    )

    if conn.is_connected():
        print('Connected to MySQL database')

        # Create a cursor object
        cur = conn.cursor()

        # Create tables and insert data
        cur.execute('''CREATE TABLE countries (
                        country_id INT,
                        country_name TEXT,
                        region_id INT
                    )''')
        cur.execute('''CREATE TABLE locations (
                        location_id INT,
                        street_address TEXT,
                        postal_code TEXT,
                        city TEXT,
                        state_province TEXT,
                        country_id INT
                    )''')
        cur.execute('''INSERT INTO countries VALUES
                        (1, 'Canada', 2),
                        (2, 'USA', 2),
                        (3, 'France', 3)''')
        cur.execute('''INSERT INTO locations VALUES
                        (1, '123 Main St', 'A1B 2C3', 'Toronto', 'Ontario', 1),
                        (2, '456 Elm St', 'X1Y 3Z6', 'Montreal', 'Quebec', 1),
                        (3, '789 Oak St', 'M4L 5T9', 'Vancouver', 'British Columbia', 2)''')

        # Query to find the address of Canada using join
        cur.execute('''SELECT locations.location_id, locations.street_address, locations.city, 
                              locations.state_province, countries.country_name
                       FROM locations
                       INNER JOIN countries ON locations.country_id = countries.country_id
                       WHERE countries.country_name = 'Canada' ''')

        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print('Error:', e)

finally:
    # Close the connection
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('Connection closed')