import pandas as pd

dict1 = {
    "id":[1,2,3,4,5],
    "name":["Ali","Sara","John","Aman","Riya"],
    "age":[20,22,21,23,20],
    "marks":[60,90,85,8,95],
    "city":["Delhi","Mumbai","Delhi","Pune","Mumbai"]
    }
df = pd.DataFrame(dict1)
print(df[df["name"].str.startswith("A")])
