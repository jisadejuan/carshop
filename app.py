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
        ],
        "Classic Sports Cars": [
            {
                "name": "Porsche 911 Classic",
                "image": "static/images/porsche-911.png",
                "price": "₱6,000,000",
                "stock": "2 units left",
                "description": "Iconic rear‑engine sports car with timeless design."
            },
            {
                "name": "Ford Mustang 1969",
                "image": "static/images/ford-mustang-1969.png",
                "price": "₱4,500,000",
                "stock": "5 units left",
                "description": "A stylish British sports car with a twin‑turbo V8 engine."
            },
            {
                "name": "Chevrolet Corvette 1963",
                "image": "static/images/chevrolet-corvette-1963.png",
                "price": "₱5,200,000",
                "stock": "3 units left",
                "description": "Classic American muscle car with roaring V8 power."
            },
            {
                "name": "Jaguar E-Type",
                "image": "static/images/jaguar-e-type.png",
                "price": "₱7,800,000",
                "stock": "2 units left",
                "description": "British classic praised for beauty and performance."
            },
            {
                "name": "Toyota 2000GT",
                "image": "static/images/toyota-2000gt.png",
                "price": "₱9,000,000",
                "stock": "1 units left",
                "description": "Rare Japanese classic, limited production sports coupe."
            }
        ],
         "Modern Supercars": [
            {
                "name": "Lamborghini Huracán EVO",
                "image": "static/images/lamborghini-huracan-evo.png",
                "price": "₱20,000,000",
                "stock": "3 units left",
                "description": "V10 supercar with advanced aerodynamics and AWD."
            },
            {
                "name": "Bugatti Chiron",
                "image": "static/images/bugatti-chiron.png",
                "price": "₱150,000,000",
                "stock": "1 unit left",
                "description": "Quad-turbo W16 hypercar, record-breaking speed and luxury."
            },
            {
                "name": "Koenigsegg Jesko",
                "image": "static/images/Koenigsegg-Jesko.png",
                "price": "₱120,000,000",
                "stock": "2 units left",
                "description": "Swedish hypercar engineered for extreme track performance."
            },
            {
                "name": "Pagani Huayra",
                "image": "static/images/pagani-huayra.png",
                "price": "₱90,000,000",
                "stock": "2 units left",
                "description": "Artful Italian hypercar with AMG V12 and bespoke design."
            },
            {
                "name": "Rimac Nevera",
                "image": "static/images/rimac_nevera.png",
                "price": "₱95,000,000",
                "stock": "3 units left",
                "description": "Electric hypercar with 1,900 hp and cutting‑edge tech."
            }
                ],
        "Track Ready Cars": [
            {
                "name": "McLaren 720S",
                "image": "static/images/McLaren_720S.png",
                "price": "₱18,000,000",
                "stock": "2 units left",
                "description": "Lightweight track monster with twin‑turbo V8."
            },
            {
                "name": "Porsche 911 GT3 RS",
                "image": "static/images/Porsche_911_GT3_RS.png",
                "price": "₱16,000,000",
                "stock": "4 units left",
                "description": "Track‑focused Porsche with naturally aspirated flat‑six."
            },
            {
                "name": "Lotus Exige",
                "image": "static/images/lotus_exige.png",
                "price": "₱7,500,000",
                "stock": "3 units left",
                "description": "Agile British sports car built for precision handling."
            },
            {
                "name": "Nissan GT-R Nismo",
                "image": "static/images/NissaN_GT-R_Nismo.png",
                "price": "₱12,500,000",
                "stock": "4 units left",
                "description": "High‑performance Japanese legend with twin‑turbo V6."
            },
            {
                "name": "BMW M4 GTS",
                "image": "static/images/BMW_M4_GTS.png",
                "price": "₱11,000,000",
                "stock": "3 units left",
                "description": "Track‑ready coupe with water‑injection turbo system."
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
