#-*- coding:utf-8 -*- 

# imports
import MySQLdb
import time
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from model.post import Post

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
        if not session.get('logged_in'):
            abort(401)
        result = Post.add(1, request.form['blog_title'], request.form['blog_content'])
        flash('add success')
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    else:
        return render_template('login.html', error=error)

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/manage/')
def manage():
    return redirect(url_for('add'))

if __name__ == '__main__':
    app.run()


