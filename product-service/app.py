from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    products.append(data)
    return jsonify({'message': 'Product added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
