#python
# Import necessary libraries
from flask import render_template, request

def home():
    """
    This function returns the home page of the web app.
    """
    return render_template('home.html')

def get_user_data():
    """
    This function retrieves user data from the form on the web page.
    It returns a dictionary of user data.
    """
    user_data = {}
    user_data['user_id'] = request.form.get('user_id')
    user_data['age'] = request.form.get('age')
    user_data['income'] = request.form.get('income')
    user_data['preferences'] = request.form.get('preferences')

    return user_data

def display_recommendations(recommendations):
    """
    This function displays the recommendations on the web page.
    It takes a list of recommendations as input.
    """
    return render_template('recommendations.html', recommendations=recommendations)

def display_history(history):
    """
    This function displays the user's recommendation history on the web page.
    It takes a list of history as input.
    """
    return render_template('history.html', history=history)

