import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create data
d = {'years_experience': [1.1,1.3,1.5,2,2.2,2.9,3.2,3.7,3.9,4.5,4.9,
                          5.1,5.3,5.9,6,7.9,8.2,8.7,9,9.6,10.3,10.5],
     'salary': [39343,46205,37731,43525,39891,56642,64445,57189,63218,61111,
                67938,66029,83088,81363,93940,101302,113812,109431,105582,
                112635,122391,121872]}
df = pd.DataFrame(data=d)

# Split data
X = pd.DataFrame(df.years_experience)
y = pd.DataFrame(df.salary)

# Fit regression
reg = LinearRegression().fit(X,y)  #<-- We're going to pickle this in a minute

print(f"Coefficient: {round(reg.coef_[0][0],2)}")  # 9267.24
print(f"Intercept: {round(reg.intercept_[0],2)}")  # 27178.6

# Pickle the regression model object
with open("pickled_model.p", "wb") as p:
    pickle.dump(reg, p)