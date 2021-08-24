# Customer details
import mysql.connector

def view_customer():
    print('Customer view screen')
    print('Enter customer id : ')
    custID = input()
    return custID

def sql_connection(custID):
    cnx = mysql.connector.connect(user='retail_user',
                                  host='localhost',
                                  password='batu',
                                  database='retail_db')
    cursor = cnx.cursor()

    query = ("SELECT * FROM customers WHERE customer_id = %s")

    cursor.execute(query, [custID])

    for val1, val2, val3, val4, val5, val6, val7, val8, val9 in cursor:
        print('Employee details: ')
        print(val1, val2, val3, val4, val5, val6, val7, val8, val9)

    cursor.close()
    cnx.close()