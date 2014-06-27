import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SECRET_KEY']='ceva secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/student/osss-web/db.sqlite'
db=SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

@app.route('/save', methods=['POST'])
def save():
    print "saving...", flask.request.form['name']
    product = Product(name=flask.request.form['name'])
    #Adaugam in baza de date
    db.session.add(product)
    db.session.commit()
    flask.flash("saved")
    return flask.redirect('/')
@app.route('/edit/<int:product_id>')
def edit(product_id):
    product=Product.query.get(product_id)
    return 'editing %r' % product
@app.route('/')
def home():
    return flask.render_template('home.html', product_list=Product.query.all())
db.create_all()
app.run(debug=True)
