import os
from flask import Flask,flash, render_template_string, render_template, jsonify, request, send_from_directory, redirect, url_for
import random


app = Flask(__name__)
app.secret_key = "ptF1uZ2Ws0eQH3gMiu0ITYs3oi8lnDuSx3hAczcRxq4vDNVAGZMwzCSuMyHSbchikTVHsGcDtTkkYPFGH2uwPJLZVNHsvtC8lCETUBYuQp2Hd7ulHP0NuXZu2GGNPgt7"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
   return render_template('index.html')

@app.errorhandler(403)
def custom403(error):
    return jsonify({'Error': error.description})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/success', methods=['POST'])
def success():
    name = request.form.get('name')
    challengequality = request.form.get('challengequality')
    othercomments = request.form.get('othercomments')
     
    if name:
        bad_chars = [*"'_#&;"]
        if any(char in bad_chars for char in name):
            random.shuffle(bad_chars)
            flash(f"The following characters are not allowed: {''.join(bad_chars)}")
            app.logger.warning(f"Filtered: {name}")
            return redirect(url_for('index'))
        elif len(name)>33:
            flash(f"Name max length is 33")
            app.logger.warning(f"Name length restriction")
            return redirect(url_for('index'))
        #saving feedback to db
        if challengequality:
            open('/dev/null', 'w').write(challengequality)
        if othercomments:
            open('/dev/null', 'w').write(othercomments)
        app.logger.warning(name)
        template = open('templates/success.html', 'r').read()
        template = template.replace("{{ name }}", name)
        
        return render_template_string(template)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
   app.run()
