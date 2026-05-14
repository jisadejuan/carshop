from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('public/index.html')

@app.route('/Products')
def products():
    categories = {
        "Luxury Sports Cars": [
            {
                "name": "Ferrari F8 Tributo",
                "image": "static/images/Ferrari_F8_Tributo.png",
                "price": "₱15,000,000",
                "stock": "3 units left",
                "description": "Twin-turbo V8 delivering 710 hp with breathtaking design."
            },
            {
                "name": "Aston Martin Vantage",
                "image": "static/images/Aston_martin.png",
                "price": "₱12,000,000",
                "stock": "5 units left",
                "description": "A stylish British sports car with a twin‑turbo V8 engine."
            },
            {
                "name": "Maserati MC20",
                "image": "static/images/maserati_mc20.png",
                "price": "₱14,500,000",
                "stock": "2 units left",
                "description": "Carbon‑fiber supercar with Nettuno V6 engine."
            },
            {
                "name": "Bentley Continental GT",
                "image": "static/images/bentley_continental.png",
                "price": "₱10,800,000",
                "stock": "4 units left",
                "description": "Luxury grand tourer with handcrafted interior and W12 engine."
            },
            {
                "name": "Lexus LC 500",
                "image": "static/images/lexus-lc500.png",
                "price": "₱9,500,000",
                "stock": "6 units left",
                "description": "Japanese luxury coupe with naturally aspirated V8."
            }
        ]
    }

    return render_template('public/products.html', categories=categories)

@app.route('/About')
def about():
    return render_template('public/about.html')

@app.route('/Categories')
def categories_page():
    return render_template('public/categories.html')

@app.route('/Contact')
def contact():
    return render_template('public/contact.html')

@app.route('/Login')
def login():
    return render_template('public/login.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
