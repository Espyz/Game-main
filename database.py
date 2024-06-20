import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="game", user="espyz", password="Ilx1dzw8SFzfPc1F", host="81.177.140.38")
        self.conn.autocommit = True

    def query(self, request, params = []):
        cursor = self.conn.cursor()
        if len(params) == 0:
            cursor.execute(request)
        else:
            cursor.execute(request, params)
        return cursor.fetchall()    
    
    def release(self):
        self.conn.close()
        