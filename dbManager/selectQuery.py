from mysql.connector import MySQLConnection, Error
from dbManager.python_mysql_dbconfig import read_db_config


def getresutls(sql):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
