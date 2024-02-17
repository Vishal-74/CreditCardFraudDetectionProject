# Credit Card Fraud Detection

## Overview

This repository focuses on predicting fraudulent credit card transactions using machine learning models. The dataset, available on [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud), comprises 284,807 transactions, including 492 fraudulent ones. Preprocessing is necessary due to data imbalance.

![1_Lci4cCUXgb6zZRyKmgWfVA](https://github.com/Vishal-74/CreditCardFraudDetectionProject/assets/115347234/fa9c32df-4f44-4dbd-9caf-73f84f506d97)

![image](https://github.com/Vishal-74/CreditCardFraudDetectionProject/assets/115347234/d3a901d7-9d8d-491a-99b5-577463d5b8c7)



## Business Problem

Banking fraud, causing significant financial losses and trust issues, was estimated at $30 billion globally by 2020 ([Nilson Report](https://nilsonreport.com/upload/content_promo/The_Nilson_Report_Issue_1164.pdf)). Rising digital transactions have led to evolving fraud methods.

## Fraud Understanding

Fraudulent activities involve unauthorized financial gains, commonly through card skimming, counterfeit cards, or stolen cards. Machine learning aids in proactive fraud monitoring, reducing manual reviews and ensuring transaction legitimacy.

## Data Details

The dataset includes transactions by European cardholders in September 2013. It's imbalanced, with 0.172% fraud cases. Principal Component Analysis (PCA) ensures confidentiality. 'Time' denotes transaction seconds, 'amount' signifies transaction value, and 'class' labels fraud (1) and non-fraud (0).

## Project Pipeline

1. **Data Understanding:** Explore and select features for the final model.
2. **Exploratory Data Analysis (EDA):** Analyze, transform, and address data skewness.
3. **Train/Test Split:** Split data using k-fold cross-validation.
4. **Model Building/Tuning:** Experiment, fine-tune models, and explore sampling techniques.
5. **Model Evaluation:** Emphasize accurate fraud identification due to data imbalance, using appropriate evaluation metrics.
