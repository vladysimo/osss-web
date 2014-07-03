#My first flask app

import flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'ceva secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/vlad/development/osss-web/osss-web/db.sqlite'

db = SQLAlchemy(app)
Bootstrap(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    description = db.Column(db.String)

#Home

@app.route('/')
def home():
    return flask.render_template('home.html', product_list=Product.query.all())

#Saving a product

@app.route('/save', methods=['POST'])
def save():
    product = Product(name=flask.request.form['name'], price=flask.request.form['price'],
            description = flask.request.form['description'])

    db.session.add(product)
    db.session.commit()

    return flask.redirect('/')

#Editing a product will require POST and GET

@app.route('/edit/<int:product_id>', methods=['POST', 'GET'])
def edit(product_id):

    product = Product.query.get(product_id)

    if not product:
        flask.abort(404)

    if flask.request.method == 'POST':

        if 'delete' in flask.request.form:
            db.session.delete(product)
        else:

            product.name=flask.request.form['name']
            product.price=flask.request.form['price']
            product.description=flask.request.form['description']

            flask.flash("product edited")

        db.session.commit()
        return flask.redirect('/')

    return flask.render_template('edit.html', product = product)

#json

@app.route('/api/list', methods=['POST','GET'])
def api_list():
  
    product_id_list = []
    product_name_list = []
    product_price_list = []
    product_description = []

    for product in Product.query.all():

        product_id_list.append(product.id)
        product_name_list.append(product.name)
        product_price_list.append(product.price)
        product_description.append(product.description)

    return flask.jsonify({
        'id_list' : product_id_list , 'name' : product_name_list , 'price' : product_price_list
        , 'description' : product_description })

#afisam un produs dupa id

@app.route('/api/product/<int:product_id>')
def api_product(product_id):

    product = Product.query.get(product_id)
    return flask.jsonify({
        'id' : product.id, 'name' : product.name})

#add an user to db

@app.route('/api/product/create', methods=['POST'])
def api_product_create():

    produs = flask.request.get_json()
    product = Product(name=produs['name'],price=produs['price'], description=produs['description'])

    db.session.add(product)
    db.session.commit()

    return flask.jsonify({'status': 'ok', 'id' : product.id})

#update user details

@app.route('/api/product/<int:product_id>/update', methods=['POST'])
def api_produs_update(product_id):

    produs = flask.request.get_json()
    product = Product.query.get(product_id)

    product.name = produs['name']
    product.price = produs['price']
    product.description = produs['description']

    db.session.commit()
    return flask.jsonify({'status' : 'ok'})



db.create_all()
app.run(debug=True)

#Pentru a folosi baza de date in shell
#sqlite3 db.sqlite
#select * from product;
