# Projects-for-SVM

This contains everything I have done regarding SVM, including "Support Vector Machine.ipynb" which contains detailed notes on the working of SVM and the creation of a pseudo SVM machine made by us.

The "SVM Code Breakdown.pdf" is where i printed the results of all the processes that take place. This was just to have a deeper understanding of the code. This is in pdf format as the file was way too big in .ipynb format

## Project :

Dataset to use
In this part we will start with 2 types of problem for the SVM algorithm
1) First SVM for Classification : We are using the “Social Network Ads” dataset on kaggle here is the link of this dataset Social_Network_Ads.The dataset is composed of 5 columns known as [User ID, Gender, Age, Estimated Salary and Purchased] and 400 row

2) Second SVM for Regression : We are using the “Position Salaries” dataset on kaggle here is the link of this dataset Position_Salaries.The dataset is composed of 3 columns known as [Position, Level and Salary] and 10 row

## Aim :

Classification :
Visualize and identify each class of the different classes and draw the dividing line by each dataset for testing

Regression :
Visualize the data points and draw the regression line and predict the salary of an employee at level 4.5 and 8.5

## Steps to follow :

#### Classification

-Import the necessary libraries
-Import the dataset and identify the data and labels (matrix X and vector Y)
-Divide data into training and test sets for data and labels
-Establish features scaling if needed
-Create a SVC object for Classification from SVM library
-Fit the dataset (training set)
-Predict the result (test set)
-Evaluate the model

#### Regression

-Import the necessary libraries
-Import the dataset
-Establish features scaling if needed
-Create a SVR object for Regression from SVM library
-Fit the dataset
-Predict the result

## Result :

#### Classification: 

We are going to visualize the test set using the linear and non-linear kernels

#### Regression :

The predictions of the value 4.5 is 115841.63 and 8.5 is 403162.82 
