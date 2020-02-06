# Create a table with a large number of records (you can find it with a google search or use this
# link - https://github.com/datacharmer/test_db). Use MySQL Database.One can setup MySQL on
# localhost. Write some basic queries using python. Suppose you want to process/fetch a large
# number of records using python while keeping your memory usage low. Think of approaches on
# how to accomplish this and Implement.
# Hint: Use Generator

import mysql.connector
from mysql.connector import Error
import sys

try:

    def ResultIter(cursor, arraysize=100):
        'An iterator that uses fetchmany to keep memory usage down'
        while True:
            results = cursor.fetchmany(arraysize)
            print(sys.getsizeof(results))
            if not results:
                break

            # Generator to send result
            for result in results:
                yield result

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees"
    )

    mycursor = conn.cursor()
    mycursor.execute("select * from dept_manager")

    for result in ResultIter(mycursor):
        print(result)


except mysql.connector.Error as error:
    print("Failed to connect to MySQL: {}".format(error))

if (conn.is_connected()):
    mycursor.close()
    conn.close()
    print("MySQL connection is closed")
