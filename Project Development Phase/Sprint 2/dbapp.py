import ibm_db

hostname="125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
uid="tbg49991"
pwd="LuEX5CZwsLRlEJK5"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port=30426
protocol="TCPIP"
cert=certificate.crt

dsn=(
     "DATABASE={0};"
     "HOSTNAME={1};"
     "PORT={2};"
     "UID={3};"
     "SECURITY=SSL;"
     "SSLServerCertificate={4};"
     "PWD={5};"
     ).format(hostname,uid,pwd,driver,db,port,protocol)
print(dsn)
try:
    db2=ibm_db.pconnect(dsn,"","")
    print("Connected to data base")
except:
    print("Unable to connect",ibm_db.conn_errormsg())
    
    