
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge,Lasso,ElasticNet,RidgeCV,LassoCV,ElasticNetCV,LinearRegression
from sklearn.model_selection import train_test_split



model = pickle.load(open('lasso Linear Regression Homework Model for deployment','rb'))
scaler = pickle.load(open('Scaler for lasso Linear Regression Homework Model for deployment','rb'))

test = [308.6,1551,42.8,0,0,0,0,0,0]
test = scaler.transform([test])
prediction = model.predict(test)
print(prediction)