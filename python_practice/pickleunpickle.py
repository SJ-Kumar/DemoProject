import pickle
import pandas as pd

# New data
d = {'years_experience': [3,3.2,4,4,4.1,6.8,7.1,9.5],
     'salary': [60150,54445,55794,56957,57081,91738,98273,116969]}
test = pd.DataFrame(data=d)

# Separate data into X and y
X_test = pd.DataFrame(test.years_experience)
y_test = pd.DataFrame(test.salary)

# Unpickle the regression model object
with open("pickled_model.p", "rb") as p:
    new_reg = pickle.load(p)

print(f"Coefficient: {round(new_reg.coef_[0][0],2)}")  # 9267.24
print(f"Intercept: {round(new_reg.intercept_[0],2)}")  # 27178.6


# R-Squared
r_squared = new_reg.score(X_test, y_test)
print(f"R-Squared: {round(r_squared*100, 2)}")  # 93.95

# Predictions
preds = new_reg.predict(X_test)

# MAPE
mape = abs((y_test - preds)/y_test).mean()
print(f"MAPE: {round(mape[0]*100, 2)}%")  # 7.96%