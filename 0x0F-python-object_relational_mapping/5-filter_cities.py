#!/usr/bin/python3
"""
That takes in the name of a state as an argument and lists all cities of that
state, using the given database where name matches the argument
Safe from SQL injection
"""

import sys
import MySQLdb

if __name__ == '__main__':
    ''' Get MySQL commands from Command-line arguments '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    ''' Connect to MySQL server '''
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    ''' Create a cursor object to execute quries '''
    cursor = conn.cursor()

    ''' Execute the query to fetch all states '''
    query = "SELECT ci.name FROM cities ci JOIN states st ON"
    query += " ci.state_id = st.id WHERE st.name = %s ORDER BY ci.id ASC"
    cursor.execute(query, (state_name,))

    ''' Fetch all rows and store the city names in a list'''
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]

    ''' Print the cities separeted by comma '''
    print(", ".join(city_names))

    ''' close the cursor and db connection '''
    cursor.close()
    conn.close()
