# import psycopg2

# class Database:
#     def __init__(self):
#         self.conn = psycopg2.connect(dbname="game", user="espyz", password="33215033q", host="localhost")
#         self.conn.autocommit = True

#     def query(self, request, params = []):
#         cursor = self.conn.cursor()
#         if len(params) == 0:
#             cursor.execute(request)
#         else:
#             cursor.execute(request, params)
#         return cursor    
    
#     def release(self):
#         self.conn.close()
        