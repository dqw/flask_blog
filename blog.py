#-*- coding:utf-8 -*- 

# imports
import MySQLdb
import time
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from model.post import Post
from model.user import User
import pdb
#pdb.set_trace()

app = Flask(__name__)
app.config.from_object("config")

@app.route('/')
def index():
    blogs = Post.get_list()
    return render_template('index.html', blogs=blogs)

@app.route('/detail/<blog_id>', methods=['GET'])
def detail(blog_id):
    blog = Post.get(blog_id)
    return render_template('detail.html', blog=blog)

@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if not session.get('user_id'):
            abort(401)
        result = Post.add(1, request.form['blog_title'], request.form['blog_content'])
        flash('add success')
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    error = None
    if request.method == 'POST':
        if User.exist(request.form['username']):
            error = "username exist"
            return render_template('sign_up.html', error=error)
        else:
            result = User.add(request.form['username'], request.form['password'])
            flash('sign up success')
            return redirect(url_for('index'))
    else:
        return render_template('sign_up.html', error=error)

@app.route('/hello/', methods=['GET'])
def hello():
    return 'Hello'

@app.route('/username/<username>', methods=['GET'])
def username(username):
    if User.exist(username):
        return 'true'
    else:
        return 'false'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.verify(request.form['username'], request.form['password'])
        if user:
            session['user_id'] = user['user_id'] 
            session['user_name'] = user['user_name'] 
            session['user_nickname'] = user['user_nickname'] 
            #pdb.set_trace()
            return redirect(url_for('index'))
        else:
            flash('You were logged in')
            return redirect(url_for('login'))
    else:
        return render_template('login.html', error=error)

@app.route('/logout/')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_nickname', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/manage/')
def manage():
    return redirect(url_for('add'))

if __name__ == '__main__':
    app.run()


