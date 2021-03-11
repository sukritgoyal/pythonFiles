from sklearn import linear_model
import pandas as pd
from word2number import w2n
df = pd.read_csv("hiring.csv")
reg = linear_model.LinearRegression()
df["test_score(out of 10)"] = df["test_score(out of 10)"].fillna(df["test_score(out of 10)"].median())
df["experience"] = df["experience"].fillna("zero")
df["experience"] = list(map(w2n.word_to_num,df["experience"]))
reg.fit(df[["experience","test_score(out of 10)", "interview_score(out of 10)"]],df["salary($)"])
print(reg.predict([[2,9,6]]))
print(reg.predict([[12,10,10]]))
