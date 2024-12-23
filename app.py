from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS for handling cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """
    Endpoint to retrieve a list of sample recipes.
    """
    sample_recipes = [
        {"id": 1, "name": "Pasta", "ingredients": ["Tomato", "Cheese", "Pasta"]},
        {"id": 2, "name": "Salad", "ingredients": ["Lettuce", "Tomato", "Cucumber"]}
    ]
    return jsonify(sample_recipes)

@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    """
    Endpoint to add a new recipe.
    """
    new_recipe = request.json
    # In a real app, save new_recipe to a database
    return jsonify({"message": "Recipe added successfully!", "recipe": new_recipe}), 201

if __name__ == '__main__':
    app.run(debug=True)
