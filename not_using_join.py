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

        # Create tables
        cur.execute('''CREATE TABLE countrie (
                        country_id INT,
                        country_name VARCHAR(100),
                        region_id INT
                    )''')
        cur.execute('''CREATE TABLE location (
                        location_id INT,
                        street_address VARCHAR(100),
                        postal_code VARCHAR(50),
                        city VARCHAR(50),
                        state_province VARCHAR(50),
                        country_id INT
                    )''')

        # Insert data into countries table
        cur.execute('''INSERT INTO countrie (country_id, country_name, region_id) VALUES 
                        (1, 'Canada', 2),
                        (2, 'USA', 2),
                        (3, 'France', 3)''')

        # Insert data into locations table
        cur.execute('''INSERT INTO location (location_id, street_address, postal_code, city, state_province, country_id) VALUES 
                        (1, '123 Main St', 'A1B 2C3', 'Toronto', 'Ontario', 1),
                        (2, '456 Elm St', 'X1Y 3Z6', 'Montreal', 'Quebec', 1),
                        (3, '789 Oak St', 'M4L 5T9', 'Vancouver', 'British Columbia', 2)''')

        # Query to find the address of Canada without using join
        cur.execute('''SELECT location_id, street_address, city, state_province, country_name
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