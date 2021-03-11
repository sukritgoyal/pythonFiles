import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
data = {"area":[2600,3000,3200,3600,4000],"price":[550000,565000,610000,680000,725000]}
df = pd.DataFrame(data)
predictData = {"area":[1000,1500,2300,3540,4120,4560,5490,3460,4750,2300,9000,8600,7100]}
pdf = pd.DataFrame(predictData)
plt.xlabel("Area(sq. feet)")
plt.ylabel("Price(US$)")
plt.scatter(df.area,df.price,color="red",marker="+")
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
p = reg.predict(pdf)
pdf["price"] = p
plt.plot(df.area, reg.predict(df[["area"]]),color="blue")
plt.show()
