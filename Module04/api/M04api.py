
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(80), unique = True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"id {self.id}, book_name {self.book_name}, author {self.author}, publisher{self.publisher}"
    
@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'id': book.id,'name': book.book_name, 'author':book.author, 'publisher':book.publisher}
        output.append(book_data)
    return {"Books": output}
@app.route("/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author":book.author, 'publisher':book.publisher}
@app.route('/books', methods = ['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'],author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id' : book.id}
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "404"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!"}
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = {"id" : id, "book_name" : request.json['book_name'],"author" :request.json['author'], "publisher" : request.json['publisher']}
    book.book_name = data.update('book_name', book.book_name)
    book.author = data.update('author', book.author)
    book.publisher = data.update('publisher', book.publisher)

    db.session.commit()
    return {'message': 'Book updated successfully', 'book': id}, 200
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
