#python
# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler

def process_data(user_data):
    """
    This function processes the user data to be used by the machine learning model.
    It takes a dictionary of user data as input and returns a pandas DataFrame.
    """

    # Convert the user data into a pandas DataFrame
    user_df = pd.DataFrame([user_data])

    # Define the columns that need to be scaled
    scale_columns = ['age', 'income']

    # Scale the necessary columns
    scaler = StandardScaler()
    user_df[scale_columns] = scaler.fit_transform(user_df[scale_columns])

    # Convert categorical columns to dummy variables
    user_df = pd.get_dummies(user_df, drop_first=True)

    return user_df

