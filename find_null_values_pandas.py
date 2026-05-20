import pandas as pd

dict1 = {
    "id":[1,2,3,4,5],
    "name":["Ali","Sara","John","Aman","Riya"],
    "age":[20,22,None,23,20],
    "marks":[85,90,78,88,95],
    "city":["Delhi",None,"Delhi","Pune","Mumbai"]
    }
df = pd.DataFrame(dict1)
print(df)
print(df.isnull())
