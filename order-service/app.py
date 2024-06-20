from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    orders.append(data)
    return jsonify({'message': 'Order placed successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
