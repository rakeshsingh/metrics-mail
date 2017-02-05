from flask import request, session, g, redirect, url_for, abort, \
     render_template, flash
from mailer import app, utils

#views
@app.route('/')
def show_datasets():
    db = utils.get_db()
    cur = db.execute('select name, data from datasets order by id desc')
    datasets = cur.fetchall()
    return render_template('show_datasets.html', datasets=datasets)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = utils.get_db()
    db.execute('insert into datasets (name, data) values (?, ?)',
                 [request.form['name'], request.form['data']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_datasets'))

@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('show_datasets'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_datasets'))
