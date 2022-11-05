import os
from flask import Flask, render_template, session, url_for, request, abort, redirect, make_response
import os
from string import ascii_lowercase
from random import seed, randbytes, choice


app = Flask(__name__)
app.secret_key = b"\x13x"

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        session.clear()
        name = request.form['name']
        session['name'] = "admin"
        print(session.values)
        return make_response(render_template('index.html'))
    else:
        name = session.get('name')
        if name and name == "admin":
            print(session.values)
            return make_response(render_template('index.html'))
        elif name:
            print(session.values)
            return make_response(render_template('index.html'))
        else:
            print(session.values)
            return make_response(render_template('index.html'))

@app.route('/unregister', methods=['GET'])
def unregister():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True)