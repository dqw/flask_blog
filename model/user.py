#-*- coding:utf-8 -*-

from MySQLdb import IntegrityError
import time
import random
import hashlib   
import pdb

from conn import db_conn
import config

class User(object):
    
    @classmethod
    def get(self, id):
        cur = db_conn.execute('select user_id, user_name, user_nickname, user_password, user_password_salt from fb_user where user_id = %s' % id)
        user = cur.fetchone()
        return user

    @classmethod
    def add(self, user_name, user_password):
        cursor = None
        try:
            user_password_salt_array = random.sample('abcdefghijklmnopqrstuvwxyz', 6) 
            user_password_salt = ''.join(user_password_salt_array)
            new_user_password = hashlib.md5(user_name + user_password_salt).hexdigest();
            current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            #pdb.set_trace()
            db_conn.execute('insert into fb_user (user_name, user_password, user_password_salt, sign_up_time, last_log_in) values (%s, %s, %s, %s, %s)',
                [user_name, new_user_password, user_password_salt, current_time, current_time ])
            db_conn.commit()
        except IntegrityError:
            db_conn.rollback()
        finally:
            cursor and cursor.close()
