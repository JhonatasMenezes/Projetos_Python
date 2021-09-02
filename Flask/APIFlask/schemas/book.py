from marshmallow import EXCLUDE
from ma import ma
from models.book import BookModel

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Beta:
        model = BookModel
        load_instance = True
        unknown = EXCLUDE