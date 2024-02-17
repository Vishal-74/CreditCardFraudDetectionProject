#streamlit run "C:/Users/Ashish/Desktop/python/Machine Learning Model/CreditCard/ccfd_streamlit.py"

import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open('ccfdtrained_model.sav', 'rb'))

# Creating a function for prediction
def credit_card_fraud_detection(input_data):
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    # Giving a title
    st.title('Credit Card Fraud Detection Web App')
    
    # Getting the input data from the user
    features = {}  # Dictionary to store input features
    
    # Define the input features and their names
    input_features = [
        ('Time', 'float'), ('Amount', 'float'), ('V1', 'float'), ('V2', 'float'), ('V3', 'float'),
        ('V4', 'float'), ('V5', 'float'), ('V6', 'float'), ('V7', 'float'),
        ('V8', 'float'), ('V9', 'float'), ('V10', 'float'), ('V11', 'float'),
        ('V12', 'float'), ('V13', 'float'), ('V14', 'float'), ('V15', 'float'),
        ('V16', 'float'), ('V17', 'float'), ('V18', 'float'), ('V19', 'float'),
        ('V20', 'float'), ('V21', 'float'), ('V22', 'float'), ('V23', 'float'),
        ('V24', 'float'), ('V25', 'float'), ('V26', 'float'), ('V27', 'float'),
        ('V28', 'float')
    ]
    
    for feature_name, feature_type in input_features:
        input_value = st.text_input(f'{feature_name} ({feature_type})')
        features[feature_name] = input_value
    
    # Code for Prediction
    transaction = ''
    
    # Creating a button for Prediction
    if st.button('Transaction Result'):
        try:
            # Convert input values to the appropriate data types
            input_data = {feature: float(value) for feature, value in features.items()}
            result = credit_card_fraud_detection(list(input_data.values()))
            if result == 0:
                transaction = 'The transaction is most likely legitimate.'
            else:
                transaction = 'The transaction could be fraudulent.'
        except ValueError:
            transaction = 'Please fill in all input fields with valid numeric values.'
        
        st.success(transaction)

if __name__ == '__main__':
    main()
