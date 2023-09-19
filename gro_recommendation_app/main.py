#python
# Import necessary libraries
from flask import Flask, request, jsonify
import data_processing as dp
import machine_learning as ml
import user_interface as ui
import database as db

app = Flask(__name__)

@app.route('/')
def home():
    return ui.home()

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user data from the request
    user_data = request.get_json()

    # Process the user data
    processed_data = dp.process_data(user_data)

    # Get recommendations using the machine learning model
    recommendations = ml.get_recommendations(processed_data)

    # Save the recommendations to the database
    db.save_recommendations(user_data['user_id'], recommendations)

    # Return the recommendations as a JSON response
    return jsonify(recommendations)

@app.route('/history', methods=['GET'])
def history():
    # Get user id from the request
    user_id = request.args.get('user_id')

    # Retrieve the user's recommendation history from the database
    history = db.get_history(user_id)

    # Return the history as a JSON response
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)

