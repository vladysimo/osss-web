#My first flask app

import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'ceva secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/student/osss-web/db.sqlite'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

#Home

@app.route('/')
def home():
    return flask.render_template('home.html', product_list=Product.query.all())

#Saving a product

@app.route('/save', methods=['POST'])
def save():
    product = Product(name=flask.request.form['name'])
    db.session.add(product)
    db.session.commit()
    flask.flash("product saved")
    return flask.redirect('/')

#Editing a product will require POST and GET

@app.route('/edit/<int:product_id>', methods=['POST', 'GET'])
def edit(product_id):
    product = Product.query.get(product_id)
    if not product:
        flask.abort(404)

    if flask.request.method == 'POST':
        product.name=flask.request.form['name']
        db.session.commit()
        return flask.redirect('/')

    return flask.render_template('edit.html', product = product)


db.create_all()
app.run(debug=True)

#Pentru a folosi baza de date in shell
#sqlite3 db.sqlite
#select * from product;
