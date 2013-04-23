#-*- coding:utf-8 -*-

from MySQLdb import IntegrityError
import time

from conn import db_conn
import config

class Post(object):
    
    @classmethod
    def get_list(self):
        cur = db_conn.execute('select post_id, post_title, post_content, post_date from fb_post order by post_id desc')
        blogs = [dict(blog_id=row[0], blog_title=row[1], blog_content=row[2], blog_time=row[3]) for row in cur.fetchall()]
        return blogs


    @classmethod
    def get(self, id):
        cur = db_conn.execute('select post_title, post_content, post_date from fb_post where post_id = %s' % id)
        blog = cur.fetchone()
        return blog

    @classmethod
    def add(self, post_author, post_title, post_content):
        cursor = None
        try:
            post_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            db_conn.execute('insert into fb_post (post_author, post_date, post_title, post_content, post_modified) values (%s, %s, %s, %s, %s)',
                [post_author, post_time, post_title, post_content, post_time ])
            db_conn.commit()
        except IntegrityError:
            db_conn.rollback()
        finally:
            cursor and cursor.close()
