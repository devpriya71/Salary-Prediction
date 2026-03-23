import pandas as pd # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
import pickle
data={
    'experience':[1,2,3,4,5],
    'salary':[20000,30000,40000,50000,60000]
}
df=pd.DataFrame(data)
x=df[['experience']]
y=df['salary']
model=LinearRegression()
model.fit(x,y)
pickle.dump(model,open('model.pkl','wb'))
print("model trained and saved")