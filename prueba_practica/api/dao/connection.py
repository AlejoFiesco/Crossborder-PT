import MySQLdb

def connect_db():
    return MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '',
        db = 'Movies',
    )
