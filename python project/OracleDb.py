import cx_Oracle;
connection = cx_Oracle.connect(user="scott", password="tiger",
                               dsn="localhost:1521/orcl")
# con = cx_Oracle.connect('HR/HR@//localhost:1521/orcl')
# print(con.version)
print(connection.version)
# print(conn)
connection = cx_Oracle.connect(user="", password="",dsn="localhost/orclpdb1")
print(connection.version)