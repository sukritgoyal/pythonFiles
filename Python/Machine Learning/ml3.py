from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
df = pd.read_csv("carprices.csv")
dummies = pd.get_dummies(df["Car Model"])
merged = pd.concat([df,dummies], axis="columns")
final = merged.drop(["Car Model", "Mercedez Benz C class"], axis="columns")
reg = linear_model.LinearRegression()
reg.fit(final[["Mileage","Age(yrs)","Audi A5","BMW X5"]], final["Sell Price($)"])
print(reg.score(final[["Mileage","Age(yrs)","Audi A5","BMW X5"]], final["Sell Price($)"]))
print(reg.predict([[45000,4,0,0]]))
print(reg.predict([[86000,7,0,1]]))
