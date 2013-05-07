#-*- coding:utf-8 -*-

from MySQLdb import IntegrityError
import time
import random
import hashlib   
import pdb
#pdb.set_trace()

from conn import db_conn
import config

class User(object):
    
    @classmethod
    def get(self, id):
        cur = db_conn.execute('select user_id, user_name, user_nickname, user_password, user_password_salt from fb_user where user_id = %s' % id)
        user = cur.fetchone()
        return user

    @classmethod
    def verify(self, user_name, user_password):
        cur = db_conn.execute('select user_id, user_name, user_nickname, user_password, user_password_salt from fb_user where user_name = "%s"' % user_name)
        result = cur.fetchone()
        if result:
            user = {} 
            user['user_id'] = result[0]
            user['user_name'] = result[1]
            user['user_nickname'] = result[2]
            user['user_password'] = result[3]
            user['user_password_salt'] = result[4]
            new_user_password = hashlib.md5(user_password + user['user_password_salt']).hexdigest();
            if new_user_password == user['user_password']:
                return user
            else:
                return None
        else:
            return None

    @classmethod
    def exist(self, user_name):
        cur = db_conn.execute('select user_id from fb_user where user_name = "%s"' % user_name)
        result = cur.fetchone()
        if result:
            return True
        else:
            return False


    @classmethod
    def add(self, user_name, user_password):
        cursor = None
        try:
            user_password_salt_array = random.sample('abcdefghijklmnopqrstuvwxyz', 6) 
            user_password_salt = ''.join(user_password_salt_array)
            new_user_password = hashlib.md5(user_password + user_password_salt).hexdigest();
            current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            #pdb.set_trace()
            db_conn.execute('insert into fb_user (user_name, user_password, user_password_salt, sign_up_time, last_log_in) values (%s, %s, %s, %s, %s)',
                [user_name, new_user_password, user_password_salt, current_time, current_time ])
            db_conn.commit()
        except IntegrityError:
            db_conn.rollback()
        finally:
            cursor and cursor.close()
