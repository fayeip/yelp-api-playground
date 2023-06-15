from flask_sqlalchemy import SQLAlchemy
from phonenumbers import parse, format_number, PhoneNumberFormat 


db = SQLAlchemy()


class Business(db.Model):
    """Business"""

    __tablename__ = 'businesses'

    business_id = db.Column(db.String, primary_key=True)
    alias = db.Column(db.String)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    is_closed = db.Column(db.Boolean)
    yelp_url = db.Column(db.String)
    review_count = db.Column(db.Integer)
    rating = db.Column(db.Float)
    coordinates_latitude = db.Column(db.Float)
    coordinates_longitude = db.Column(db.Float)
    address_street = db.Column(db.String)
    address_city = db.Column(db.String)
    address_state = db.Column(db.String)
    address_zip = db.Column(db.Integer)
    display_phone = db.Column(db.String)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))

    city = db.relationship('City', back_populates='business')
    categories = db.relationship('Category', secondary="businesscategories", back_populates='businesses')

    def __repr__(self):
        return f'<Business name={self.name}>'

    def to_dict(self):
        return {'business_id': self.business_id,
                'alias': self.alias,
                'name': self.name,
                'image_url': self.image_url,
                'is_closed': self.is_closed,
                'yelp_url': self.yelp_url,
                'review_count': self.review_count, 
                'rating': self.rating, 
                'coordinates_latitude': self.coordinates_latitude, 
                'coordinates_longitude': self.coordinates_longitude, 
                'address_street': self.address_street, 
                'address_city': self.address_city, 
                'address_state': self.address_state,
                'address_zip': self.address_zip, 
                'display_phone': format_phonenumber(self.display_phone) if self.display_phone else "",  
                'city_id': self.city_id,
                'categories': [cat.name for cat in self.categories]}


class City(db.Model):
    """City"""

    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    business = db.relationship('Business', back_populates='city')


    def __repr__(self):
        return f'<City name={self.name}>'

    def to_dict(self):
        return {'city_id': self.city_id,
                'name': self.name}


class Category(db.Model):
    """Category"""

    __tablename__ = 'categories'

    alias = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    businesses = db.relationship('Business', secondary="businesscategories", back_populates='categories')


    def __repr__(self):
        return f'<Category name={self.name}>'

    def to_dict(self):
        return {'alias': self.alias,
                'name': self.name}


class BusinessCategory(db.Model):
    """BusinessCategory"""

    __tablename__ = 'businesscategories'

    bc_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    business_id = db.Column(db.String, db.ForeignKey('businesses.business_id'), nullable=False)
    category_alias = db.Column(db.String, db.ForeignKey('categories.alias'), nullable=False)


    def __repr__(self):
        return f'<BusinessCategory id={self.bc_id}>'

    def to_dict(self):
        return {'bc_id': self.bc_id,
                'business_id': self.business_id, 
                'category_alias': self.category_alias}


def format_phonenumber(ph):
    return format_number(parse(ph, "US"), PhoneNumberFormat.NATIONAL) 


def connect_to_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///popups'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    db.app = app
    db.init_app(app)

    print('Connected to database!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    with app.app_context():
        db.create_all() 
