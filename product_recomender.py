import openai
import requests

class ProductRecommender:
    def __init__(self, api_key):
        self.api_key = api_key
        self.chat_models = 'text-davinci-003'
        openai.api_key = self.api_key  # Set the openai.api_key directly
        self.country = None
        self.season = None

    def set_country(self, country):
        self.country = country

    def set_season(self, season):
        self.season = season

    def get_product_recommendations(self, product_type):
        prompt = f"In the {self.season}, what type of {product_type} would you recommend for {self.country}?"
        response = openai.ChatCompletion.create(
            model=self.chat_models,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message['content']