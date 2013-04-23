#-*- coding:utf-8 -*-

# imports
import MySQLdb
import datetime
import config

def connect_db():
    return MySQLdb.connect(
            host=config.DB_HOST, 
            user=config.DB_USER, 
            passwd=config.DB_PASSWD,
            db=config.DB_NAME,
            use_unicode=True,
            charset="utf8")

class DB(object):
    
    def __init__(self):
        self._conn = connect_db()
        self._conn.select_db(config.DB_NAME)

    def connect(self):
        self._conn = connect_db()
        return self._conn

    def execute(self, *a, **kw):
        cursor = kw.pop('cursor', None)
        try:
            cursor = cursor or self._conn.cursor()
            cursor.execute(*a, **kw)
        except (AttributeError, MySQLdb.OperationalError):
            print 'debug, %s re-connect to mysql' % datetime.datetime.now()
            self._conn and self._conn.close()
            self.connect()
            cursor = self._conn.cursor()
            cursor.execute(*a, **kw)
        return cursor
        
    def commit(self):
        return self._conn and self._conn.commit()

    def rollback(self):
        return self._conn and self._conn.rollback()

db_conn = DB()


