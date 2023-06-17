import os 
import json 
import crud
import model
import server

os.system("dropdb popups")
os.system("createdb popups")

model.connect_to_db(server.app) 

with open("sample_data.json", "r") as f:
    sample_data = json.loads(f.read())

with server.app.app_context():
    model.db.create_all()

    all_biz = [] 
    all_businesscategories = [] 

    for biz in sample_data['businesses']:
        print(biz['id'])
        print(biz['alias'])
        print(biz['name'])
        print(biz['image_url'])
        print(biz['is_closed'])
        print(biz['url'])
        print(biz['review_count'])
        print(biz['rating'])
        print(biz['coordinates']['latitude'])
        print(biz['coordinates']['longitude'])
        print(biz['location']['address1'])
        print(biz['location']['city'])
        print(biz['location']['state'])
        print(biz['location']['zip_code'])
        print(biz['phone'])
        
        business = crud.create_business(biz['id'],
                                        biz['alias'],
                                        biz['name'],
                                        biz['image_url'],
                                        biz['is_closed'],
                                        biz['url'],
                                        biz['review_count'],
                                        biz['rating'],
                                        biz['coordinates']['latitude'],
                                        biz['coordinates']['longitude'],
                                        biz['location']['address1'],
                                        biz['location']['city'],
                                        biz['location']['state'],
                                        biz['location']['zip_code'],
                                        biz['phone'])
        
        for cat in biz['categories']:
            print(cat)
            category = crud.get_category_by_alias(cat['alias'])
            if not category:
                category = crud.create_category(cat['alias'], cat['title']) 
            
            all_businesscategories.append( (biz['id'], cat['alias']) ) 
        
        print(business)
        print(business.city_id)
        all_biz.append(business)
    
    model.db.session.add_all(all_biz)
    model.db.session.commit() 

    for bc in all_businesscategories:
        print("THIS IS THE BUSINESSCATEGORY")
        b_id = bc[0]
        c_alias = bc[1] 
        bc = crud.get_businesscategory(b_id, c_alias)
        if not bc:
            bc = crud.create_businesscategory(b_id, c_alias)
        print(bc)
    



        


