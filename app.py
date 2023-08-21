from flask import Flask, request, jsonify
from product_recomender import ProductRecommender
from greeter import Greeter

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend_products():
    # Parse parameters from the GET request
    country = request.args.get('country')
    season  = request.args.get('season')
    product_types = request.args.get('product_types').split(',')
    api_key = "sk-API_key"  # Replace with your actual API key
    # Create an instance of ProductRecommender
    recommender = ProductRecommender(api_key)
    recommender.set_country(country)
    recommender.set_season(season)
    recommendations = {}
    for product_type in product_types:
        recommendations[product_type] = recommender.get_product_recommendations(product_type)

    return jsonify(recommendations)


@app.route('/hello', methods=['GET'])
def greet():
    return Greeter.say_hello()  # call the say_hello method


if __name__ == "__main__":
    app.run(debug=True)
