from flask import Flask, request, jsonify

app = Flask(__name__)
books = []

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = {'id': len(books)+1, 'title': data['title'], 'author': data['author']}
    books.append(book)
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books)

@app.route('/books/<int:bid>', methods=['PUT'])
def update_book(bid):
    for b in books:
        if b['id'] == bid:
            b.update(request.get_json())
            return jsonify(b)
    return jsonify({'error': 'Book not found'}), 404
