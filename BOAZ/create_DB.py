# from tokenize import Double
# import pymysql
# import mysql.connector

# # Define a method to create a database connection
# def getDatabaseConnection(ipaddress, usr, passwd, curtype):
#     sqlCon  = mysql.connector.connect(host=ipaddress, user=usr, password=passwd)
#     return sqlCon

# # Define a method to create MySQL users
# def createUser(cursor, userName, password,
#                querynum=0, 
#                updatenum=0, 
#                connection_num=0):
#     try:
#         sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(userName, password)
#         cursor.execute(sqlCreateUser)
#         sqlCreateUser = "CREATE USER '%s'@'%' IDENTIFIED BY '%s';"%(userName, password)
#         cursor.execute(sqlCreateUser)
#         sqlCreateUser = "GRANT ALL PRIVILEGES ON '%s'.* TO '%s'@'localhost';"%(mySQLConnection, userName)
#         cursor.execute(sqlCreateUser)
#         sqlCreateUser = "FLUSH PRIVILEGES;"
#         cursor.execute(sqlCreateUser)

#     except Exception as Ex:
#         print("Error creating MySQL User: %s"%(Ex))

# # Connection parameters and access credentials
# ipaddress   = "127.0.0.1"  # MySQL server is running on local machine
# usr         = "root"       
# passwd      = ""             
# curtype    = pymysql.cursors.DictCursor    

# mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, curtype)
# mySQLCursor     = mySQLConnection.cursor()

# createUser(mySQLCursor, "test","0000")

# mySqlListUsers = "select host, user from mysql.user;"
# mySQLCursor.execute(mySqlListUsers)

# mySQLCursor.execute("CREATE DATABASE youplace")
# mySQLCursor.execute("SHOW DATABASES")


# for x in mySQLCursor:
#     print(x)