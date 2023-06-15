
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
                    address_street, 
                    address_city, 
                    address_state, 
                    address_zip, 
                    display_phone):
    
    city = get_city_by_name(address_city)
    if not city:
        city = create_city(address_city)

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
                    address_street=address_street,
                    address_city=address_city, 
                    address_state=address_state,
                    address_zip=address_zip, 
                    display_phone=display_phone, 
                    city_id=city.city_id) 

    return business


def create_category(alias, name):
    category = Category(alias=alias, name=name) 

    db.session.add(category)
    db.session.commit() 

    return category 


def create_city(name):
    city = City(name=name)

    db.session.add(city)
    db.session.commit() 

    return city 


def create_businesscategory(business_id, category_alias):
    businesscategory = BusinessCategory(business_id=business_id, category_alias=category_alias)

    db.session.add(businesscategory)
    db.session.commit() 
    
    return businesscategory


def get_city_by_name(city_name):
    return City.query.filter(City.name == city_name).first() 


def get_category_by_alias(alias):
    return Category.query.filter(Category.alias == alias).first()


def get_businesscategory(b_id, c_alias):
    return BusinessCategory.query.filter((BusinessCategory.business_id == b_id) & (BusinessCategory.category_alias == c_alias)).first()


def get_all_businesses():
    return Business.query.all() 



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
