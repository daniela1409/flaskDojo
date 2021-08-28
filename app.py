from flask import Flask
from flask_mysqldb import flask_mysqldb
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        flash('Contact added succesfully')
        return 'received'

    return 'add'

@app.route('/edit')
def edit():
    return 'edit'


@app.route('/delete')
def delete():
    return 'delete'


if __name__ == '__main__':
    app.run(port = 8080, debug = True)