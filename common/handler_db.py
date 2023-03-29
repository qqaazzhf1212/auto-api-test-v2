import pymysql


class DB:
    def __init__(self, db_config: dict):
        # 创建连接
        self.conn = pymysql.connect(**db_config)

    def get_one(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()

    def get_many(self, sql, size: int):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchmany(size)

    def exist(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            if cursor.fetchone():
                return True
            else:
                return False

    def get_all(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def __del__(self):
        self.conn.close()
        # print('关闭连接')

# if __name__ == '__main__':
#     import settings
#
#     db = DB(settings.DB_CONFIG)
#     sql = 'select * from auth_user'
#     res = db.get_one(sql)
#     print(res)
