import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, 2].values


from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(np.reshape(Y, (10,1)))

from sklearn.svm import SVR
regressor = SVR() # add this parametre kernel='linear' for a linear model
regressor.fit(X,Y.ravel())

def y_pred(x) :
    return(sc_Y.inverse_transform(regressor.predict(sc_X.transform(np.array([[x]]))).reshape(-1,1)))

# Visualisation the regression result
plt.scatter(x=X, y=Y,color='red')
plt.plot(X, regressor.predict(X), color='green')
plt.title('Truth of Bluff / SVR')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

print(y_pred(4.5))
print(y_pred(8.5))
