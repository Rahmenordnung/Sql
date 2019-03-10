import os
import pymysql

#Get username from Vloud9 workspace
#(modify this variable if runnin on another environment)
username= os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless of wheather the above was successful
    connection.close()
        