import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a sample DataFrame
data = {'X': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Y': [10, 15, 20, 25, 30, 35, 40, 45, 50]}
df = pd.DataFrame(data)

# Split the data into features (X) and target variable (y)
X = df[['X']]  # Features
y = df['Y']     # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Visualize the regression line
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Linear Regression Model')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Print the model coefficients
print('Intercept:', model.intercept_)
print('Coefficient:', model.coef_[0])

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)






df = pd.read_excel("myhome.xlsx")
print(df)
df.to_excel('Quiz.xlsx', index=False)

plt.figure(figsize=(8, 5))
plt.plot(df.index, df['ფასი'], marker='o', linestyle='-')
plt.title('Line Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['ფასი'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()