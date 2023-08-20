#!/usr/bin/python3
"""
That lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    ''' Get MySQL commands from Command-line arguments '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN "
    query += "states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    ''' Fetch all rows then display all cities in a new line'''
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    ''' close the cursor and db connection '''
    cursor.close()
    conn.close()
