from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data
quotes = [
    {
        "id": 1,
        "author": "Albert Einstein",
        "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    },
    {
        "id": 2,
        "author": "Mark Twain",
        "quote": "The secret of getting ahead is getting started.",
    },
]


@app.route("/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)


@app.route("/quotes/<int:id>", methods=["GET"])
def get_quote(id):
    quote = next((q for q in quotes if q["id"] == id))
    return jsonify(quote) if quote else "", 404


@app.route("/quotes", methods=["POST"])
def add_quote():
    new_quote = request.json
    quotes.append(new_quote)
    return jsonify(new_quote), 201


@app.route("/quotes/<int:id>", methods=["DELETE"])
def delete_quote(id):
    global quotes
    quotes = [q for q in quotes if q["id"] != id]
    return "", 204


@app.route("/quotes/<int:id>", methods=["PUT"])
def update_quote(id):
    quote = next((q for q in quotes if q["id"] == id))
    if quote:
        quote.update(request.json)
        return jsonify(quote)
    return "", 404


if __name__ == "__main__":
    app.run(debug=True)
