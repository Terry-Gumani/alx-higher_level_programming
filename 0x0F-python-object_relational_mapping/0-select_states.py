#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)
    cursor = db.cursor()

    # Execute the query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
