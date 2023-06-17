import os 
from flask import Flask, jsonify, render_template
from model import db, connect_to_db
import crud 

app = Flask(__name__)
app.secret_key = os.environ['FLASK_KEY']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/businesses')
def get_businesses():
    businesses = crud.get_all_businesses() 
    return jsonify({biz.business_id: biz.to_dict() for biz in businesses})

@app.route('/api/categories') 
def get_categories():
    categories = crud.get_all_categories()
    print(categories)
    return jsonify({category.alias: category.to_dict() for category in categories}) 

# @app.route('/api/business/<category>') 
# def get_businesses_by_category(category): 




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=5001)



