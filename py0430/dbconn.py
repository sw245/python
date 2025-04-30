import oracledb as ora

## db접속정보
def connections():
    conn = ora.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    return conn