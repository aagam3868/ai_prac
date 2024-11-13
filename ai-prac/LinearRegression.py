# # Importing necessary libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# # Generating some synthetic data
# # Let's say we're modeling a relationship like y = 2x + 3 + noise
# np.random.seed(0)
# X = 2 * np.random.rand(100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)

# # Splitting the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # Creating the linear regression model
# model = LinearRegression()

# # Fitting the model to the training data
# model.fit(X_train, y_train)

# # Making predictions on the test set
# y_pred = model.predict(X_test)

# # Printing model coefficients
# print("Intercept:", model.intercept_)
# print("Slope:", model.coef_)

# # Calculating and printing performance metrics
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R-squared:", r2)

# # Plotting the results
# plt.scatter(X, y, color="blue", label="Actual Data")
# plt.plot(X_test, y_pred, color="red", label="Predicted Line")
# plt.xlabel("X")
# plt.ylabel("y")
# plt.title("Linear Regression")
# plt.legend()
# plt.show()







# Import necessary libraries
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: X as input feature and y as target variable
X = np.array([[1], [2], [3], [4], [5]])  # Features (e.g., study hours)
y = np.array([1.5, 3.0, 4.5, 6.0, 7.5])  # Target variable (e.g., exam scores)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model on the data
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Print results
print("Intercept (b):", model.intercept_)
print("Coefficient (m):", model.coef_[0])
print("Predictions:", predictions)
