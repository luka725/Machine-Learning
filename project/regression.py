import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
df = pd.read_excel("monitors_sanitized.xlsx")

label_encoder = LabelEncoder()
df['frequency_encoded'] = label_encoder.fit_transform(df['სიხშირე'])
x = df[['frequency_encoded']]
y = df['ფასი']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
for freq in sorted(df['სიხშირე'].unique()):
    print(freq)
print(f'Mean Squared Error: {mse}')
r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2}')
plt.scatter(X_test, y_test, label='Actual Prices')
plt.plot(X_test, y_pred, color='red', label='Predicted Prices')
plt.xlabel('Frequency Encoded')
plt.ylabel('Price')
plt.title('Linear Regression: Encoded Frequency vs. Price')
plt.legend()
plt.show()