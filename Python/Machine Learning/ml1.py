from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("canada_per_capita_income.csv")
plt.xlabel("Year")
plt.ylabel("per capita income (US$)")
plt.scatter(df.year, df["per capita income (US$)"], color="red",marker="+")
reg = linear_model.LinearRegression()
reg.fit(df[["year"]],df["per capita income (US$)"])
plt.plot(df.year, reg.predict(df[["year"]]), color="blue")
plt.show()
