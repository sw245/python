import oracledb

def connections():
    try: conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn