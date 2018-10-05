from psycopg2 import connect
from  utils import env

class DBconnection():
    def get_connection(self):
        __connection = None
        conn = connect(host=env('HOST'),
                       database=env('DATABASE'),
                       user=env('USER'),
                       password=env('PASS'))
        return conn


conn = DBconnection()
print(conn.get_connection())
