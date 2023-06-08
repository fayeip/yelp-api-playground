"""CRUD operations."""

from model import db, Business, City, Category, BusinessCategory, connect_to_db


def create_business(business_id, 
                    alias, 
                    name, 
                    image_url, 
                    is_closed, 
                    yelp_url, 
                    review_count, 
                    rating, 
                    coordinates_latitude, 
                    coordinates_longitude, 
                    display_address, 
                    display_phone, 
                    city_name):
    
    city_id = get_city_by_name(city_name).city_id 

    business = Business(
                    business_id=business_id, 
                    alias=alias, 
                    name=name, 
                    image_url=image_url, 
                    is_closed=is_closed, 
                    yelp_url=yelp_url, 
                    review_count=review_count, 
                    rating=rating, 
                    coordinates_latitude=coordinates_latitude, 
                    coordinates_longitude=coordinates_longitude, 
                    display_address=display_address, 
                    display_phone=display_phone, 
                    city_id=city_id) 
    
    db.session.add(business)
    db.session.commit() 

    return business


def create_category():
    

def get_city_by_name(city_name):
    """Return city by name"""

    return City.query.filter(City.name == city_name).first() 





if __name__ == "__main__":
    from server import app

    connect_to_db(app)
