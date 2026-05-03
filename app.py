
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('public/index.html')

@app.route('/Products')
def products():
    return render_template('public/products.html')

@app.route('/About')
def about():
    return render_template('public/about.html')

@app.route('/Categories')
def categories():
    return render_template('public/categories.html')

@app.route('/Contact')
def contact():
    return render_template('public/contact.html')

@app.route('/Login')
def login():
    return render_template('public/login.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
  
