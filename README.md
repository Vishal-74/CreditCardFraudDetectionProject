# Credit Card Fraud Detection

## Problem Statement

This project's chosen problem statement is the prediction of fraudulent credit card transactions through the use of machine learning models.

In this project, we will analyze customer-level data collected and examined during a research collaboration between Worldline and the Machine Learning Group.

The dataset is sourced from the [Kaggle Website](https://www.kaggle.com/mlg-ulb/creditcardfraud) and comprises a total of 284,807 transactions, including 492 fraudulent ones. Due to a high level of imbalance in the dataset, it requires preprocessing before model development.

## Business Problem Overview

For many banks, the primary business goal is to retain high-profit customers. However, banking fraud poses a significant threat to this goal. It is a concerning issue for both banks and customers, leading to substantial financial losses, trust issues, and credibility concerns.

According to the [Nilson report](https://nilsonreport.com/upload/content_promo/The_Nilson_Report_Issue_1164.pdf), banking frauds were estimated to account for $30 billion worldwide by 2020. With the increasing use of digital payment channels, fraudulent transactions are also on the rise, employing new and diverse techniques.

In the banking sector, the use of machine learning for credit card fraud detection is not just a trend but a necessity. It enables proactive monitoring and fraud prevention mechanisms, reduces manual reviews, costly chargebacks, and denials of legitimate transactions.

## Understanding and Defining Fraud

Credit card fraud involves any dishonest act to obtain unauthorized financial gain without the account holder's permission. The most common form of fraud is skimming, where information from the magnetic strip of a card is duplicated. Other methods include manipulation of genuine cards, counterfeit card creation, using stolen/lost credit cards, and fraudulent telemarketing.

## Data Dictionary

You can download the dataset using this [link](https://www.kaggle.com/mlg-ulb/creditcardfraud).

The dataset comprises credit card transactions made by European cardholders over two days in September 2013. Out of 284,807 transactions, 492 are fraudulent. The dataset is highly unbalanced, with fraudulent transactions accounting for 0.172% of the total. Principal Component Analysis (PCA) has been applied to maintain confidentiality. All features except 'time' and 'amount' are principal components derived from PCA. 'Time' represents the seconds elapsed between the first transaction and subsequent ones, while 'amount' denotes the transaction amount. The 'class' feature indicates class labels, with 1 indicating fraud and 0 for non-fraudulent transactions.

## Project Pipeline

The project pipeline can be summarized in four main steps:

- **Data Understanding:** Load and understand the dataset's features to select those needed for the final model.
- **Exploratory Data Analysis (EDA):** Perform univariate and bivariate analyses, and consider feature transformations if required. Check for skewness in the data that might affect model-building.
- **Train/Test Split:** Split the data for model evaluation using k-fold cross-validation to ensure proper representation of the minority class in test folds.
- **Model Building/Hyperparameter Tuning:** Experiment with different models and fine-tune their hyperparameters to achieve the desired performance. Explore various sampling techniques for better results.
- **Model Evaluation:** Evaluate models using appropriate metrics, emphasizing accurate identification of fraudulent transactions due to the data's imbalance. Choose metrics that align with this business goal.
