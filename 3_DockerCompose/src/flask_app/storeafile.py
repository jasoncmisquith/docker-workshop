from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/store_file', methods=['post'])
def store_file():
    file_name = request.form.get('filename')
    if not file_name or ("." not in file_name):
        return
    file_content = request.form.get('content')
    with open('/filestore/' + file_name, 'w') as fp:
        fp.write(file_content)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

app.run(host="0.0.0.0")
 