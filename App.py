from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

customers = [
    {"name": "Rahul", "cart_value": 1999, "status": "Abandoned"},
    {"name": "Priya", "cart_value": 2499, "status": "Abandoned"},
    {"name": "Arjun", "cart_value": 999, "status": "Purchased"},
]

@app.route("/")
def home():
    total_lost = sum(
        customer["cart_value"]
        for customer in customers
        if customer["status"] == "Abandoned"
    )

    return render_template(
        "index.html",
        customers=customers,
        total_lost=total_lost
    )

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    cart_value = float(data.get("cart_value", 0))

    
    if cart_value >= 1500:
        probability = 85
    elif cart_value >= 500:
        probability = 65
    else:
        probability = 45

    return jsonify({
        "recovery_probability": probability,
        "message": "Customer has a high recovery potential."
        if probability >= 70
        else "Customer has moderate recovery potential."
    })


if __name__ == "__main__":
    app.run(debug=True)
