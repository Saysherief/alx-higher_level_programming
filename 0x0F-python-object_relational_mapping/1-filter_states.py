#!/usr/bin/python3
"""
That lists all states that start with N from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    ''' Fetch all rows then display all states in new line'''
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    ''' close the cursor and db connection '''
    cursor.close()
    conn.close()
