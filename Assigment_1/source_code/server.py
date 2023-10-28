'''
Created on Jan 10, 2017

@author: hanif
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session, jsonify
from module.database import Database

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)
    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:
        if db.update(session['update'], request.form):
            flash('A phone number has been updated')
        else:
            flash('A phone number can not be updated')
        session.pop('update', None)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:
        if db.delete(session['delete']):
            flash('A phone number has been deleted')
        else:
            flash('A phone number can not be deleted')
        session.pop('delete', None)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

# REST API endpoints
# Get all phonebook entries
@app.route('/api/phonebook', methods=['GET'])
def get_phonebook_entries():
    data = db.read(None)
    return jsonify({'entries': data})

# Get a single phonebook entry by ID
@app.route('/api/phonebook/<int:id>', methods=['GET'])
def get_phonebook_entry(id):
    data = db.read(id)
    if len(data) == 0:
        return jsonify({'error': 'Entry not found'}), 404
    return jsonify({'entry': data[0]})

# Create a new phonebook entry
@app.route('/api/phonebook', methods=['POST'])
def create_phonebook_entry():
    if request.method == 'POST' and request.json:
        if db.insert(request.json):
            return jsonify({'message': 'A new phone number has been added'}), 201
        else:
            return jsonify({'error': 'A new phone number cannot be added'}), 400
    else:
        return jsonify({'error': 'Bad request'}), 400

# Update a phonebook entry by ID
@app.route('/api/phonebook/<int:id>', methods=['PUT'])
def update_phonebook_entry(id):
    data = db.read(id)
    if len(data) == 0:
        return jsonify({'error': 'Entry not found'}), 404
    if request.method == 'PUT' and request.json:
        if db.update(id, request.json):
            return jsonify({'message': 'A phone number has been updated'}), 200
        else:
            return jsonify({'error': 'A phone number cannot be updated'}), 400
    else:
        return jsonify({'error': 'Bad request'}), 400

# Delete a phonebook entry by ID
@app.route('/api/phonebook/<int:id>', methods=['DELETE'])
def delete_phonebook_entry(id):
    data = db.read(id)
    if len(data) == 0:
        return jsonify({'error': 'Entry not found'}), 404
    if db.delete(id):
        return jsonify({'message': 'A phone number has been deleted'}), 200
    else:
        return jsonify({'error': 'A phone number cannot be deleted'}), 400

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
