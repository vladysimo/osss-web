#My first flask app

import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'ceva secret'

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/save', methods=['POST'])
def save():
    print "saving...", flask.request.form['name']
    flask.flash("product saved")
    return flask.redirect('/')

app.run(debug=True)
