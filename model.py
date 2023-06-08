from flask_sqlalchemy import SQLAlchemy


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
    display_address = db.Column(db.ARRAY(db.String)) 
    display_phone = db.Column(db.String)

    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))
    # businesscategory_id = db.Column(db.Integer, db.ForeignKey('businesscategories.bc_id'))

    city = db.relationship('City', back_populates='business')
    category = db.relationship('Category', secondary="businesscategories", back_populates='business')

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
                'display_address': self.display_address, 
                'display_phone': self.display_phone, 
                'city': self.city.city_id}


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

    business = db.relationship('Business', secondary="businesscategories", back_populates='category')


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
    category_id = db.Column(db.String, db.ForeignKey('categories.alias'), nullable=False)

    # business = db.relationship('Business', back_populates='business_category')
    # category = db.relationship('Category', back_populates='business_category')


    def __repr__(self):
        return f'<BusinessCategory id={self.bc_id}>'

    def to_dict(self):
        return {'bc_id': self.bc_id,
                'business_id': self.business_id, 
                'category_id': self.category_id}


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
