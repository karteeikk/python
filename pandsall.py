import pandas as pd
mar={
    "name":["kartik","meet","raj"],
    "age":[23,43,21]
}
df=pd.DataFrame(mar)
print(df)
print(df.loc[(df.name=="kartik")])
print(df.iloc[[0,1]])
