from flask.globals import request
from flask_restplus import Resource, fields
from marshmallow.utils import EXCLUDE

from models.book import BookModel
from schemas.book import BookSchema

from server.instance import server

book_ns = server.book_ns

book_schema = BookSchema()
book_list_schema = BookSchema(many=True)

ITEM_NOT_FOUND = 'Book not found'

item = book_ns.model('Book', {
    'title': fields.String(description='book title'),
    'pages': fields.Integer(default=0)        
})

class Book(Resource):
    
    def get(self, id):
        book_data = BookModel.find_by_id(id)
        if book_data:
            return book_schema.dump(book_data)
        return {'message': ITEM_NOT_FOUND}
        
class BookList(Resource):
    
    def get(self, ):
        return book_list_schema.dump(BookModel.find_all()), 200
    
    @book_ns.expect(item)
    @book_ns.doc('Create an item')
    def post(self, ):
        book_json = request.get_json()
        book_data = book_schema.load(book_json)
        
        book_data.save_to_db()
        
        return book_schema.dump(book_data), 201