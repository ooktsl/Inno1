import pandas as pd   # read data
from sklearn.model_selection import train_test_split  # split test train
from sklearn.ensemble import RandomForestRegressor   # train model
from sklearn.metrics import r2_score
import joblib


df = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/Advertising.csv")
print(df.head())

# Feature matrix
X = df.iloc[:, 1:-1].values
print(X.shape)
print(X[:3])

# Output variable
y = df.iloc[:, -1]
print(y.shape)
print(y[:6])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

estimator = RandomForestRegressor(n_estimators=200)
estimator.fit(X_train, y_train)

# Test model
y_pred = estimator.predict(X_test)


r2 = r2_score(y_true=y_test, y_pred=y_pred)
print(f"R2: {r2}")

# Save Model
joblib.dump(estimator, "./randomforest_with_advertising.pkl")

