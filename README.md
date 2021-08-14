# Phishing Domain Detection Using Random Forest Classifier

This web application determines if a webpage is a phishing page or not using the Random Forest Classification Algorithm. 

## Live Application
The web application is hosted at []()

## Screenshots
![Landing Page](https://github.com/abdulalikhan/Phishing-Domain-Detection/blob/main/1.png?raw=true)
![Detected a Phishing Page](https://github.com/abdulalikhan/Phishing-Domain-Detection/blob/main/2.png?raw=true)
![Detected a Safe Page](https://github.com/abdulalikhan/Phishing-Domain-Detection/blob/main/3.png?raw=true)

## Tech Stack
![Tech Stack](https://github.com/abdulalikhan/Phishing-Domain-Detection/blob/main/stack.png?raw=true)

## Model Performance

Four different machine learning algorithms were used to train our model (Random Forest, Perceptron, Linear Regression, and CART).
The table below shows the accuracy of the trained models for five different testing-training data splits.


| Algorithm                 | 50-50 Split  | 60-40 Split  | 70-30 Split  | 80-20 Split  | 90-10 Split  |
| ------------------------- | ------------------------------------------------------------------------:|
| Logistic Regression       | 78.09%       | 78.02%       | 78.35%       | 78.43%       | 80.83%       |
| Random Forest             | 85.11%       | 84.58%       | 85.71%       | 85.48%       | 88.52%       |
| Perceptron                | 68.90%       | 74.36%       | 72.41%       | 68.11%       | 73.33%       |
| C.A.R.T.                  | 84.53%       | 84.35%       | 85.26%       | 84.71%       | 87.70%       |

The model trained using the Random Forest Classification Algorithm was selected as it consistently provided the highest accuracy (between 85% and 88%)

### Mean Absolute Percentage Errors

To determine the accuracy of the models, I calculated the Mean Absolute Percentage Error using the predicted and actual closing price values for the testing data.

| Algorithm                 | 50-50 Split                     |
| ------------------------- | -------------------------------:|
| Logistic Regression       | 8.71%                           |
| Random Forest             | 4.94%                           |
| Perceptron                | 14.99%                          |
| C.A.R.T.                  | 10.70%                          |
