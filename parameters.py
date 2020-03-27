import pymysql

MYSQL_HOST = "database-1.cszampg2p55a.us-east-1.rds.amazonaws.com"
MYSQL_USERNAME = "admin"
MYSQL_PASSWORD = "Lakshman4"
MYSQL_DATABASE = "BillingSystem"
mysqlConn = pymysql.connect(host=MYSQL_HOST, port=3306, user=MYSQL_USERNAME, password=MYSQL_PASSWORD,
                             database=MYSQL_DATABASE,autocommit=True)
