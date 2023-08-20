#!/usr/bin/python3
"""
That takes in an argument and displays all values in the states table of
the given database where name matches the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    ''' Get MySQL commands from Command-line arguments '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY
    id ASC".format(state)
    cursor.execute(query)

    ''' Fetch all rows then display all states in new line'''
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    ''' close the cursor and db connection '''
    cursor.close()
    conn.close()
