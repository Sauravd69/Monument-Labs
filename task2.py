import pymysql
from intercom.client import Client

#connect to the database
conn = pymysql.connent(host='localhost',user='root',password='',db='InnoDB')
cur = conn.cursor()

query = 'SELECT * FROM USER;'
row = cur.execute(query)

#we have at least one row/user
if row!=0:
    #fetching all informations
    data = cur.fetchall()
    for info in data:
        #info is one row of the result
        #inside a row there are 3 columns: id, name, email
        #creating an account for a user using those information
        intercom.users.create(id=info[0], name=info[1], email=info[2])

#close the connection
conn.close()
