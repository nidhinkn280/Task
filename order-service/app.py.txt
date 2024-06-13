from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {"id": 1, "user_id": 1, "product_id": 101, "quantity": 2},
    {"id": 2, "user_id": 2, "product_id": 102, "quantity": 1}
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order["id"] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.json
    orders.append(new_order)
    return jsonify(new_order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
