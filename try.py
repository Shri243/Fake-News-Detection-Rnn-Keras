import pandas as pd 
df_true = pd.read_csv("True.csv")
i = 20
a = df_true.title
b = df_true.text
print("\n\n",a[i],"\n\n")
print(str(b[i]))

Falsex = pd.read_csv("Fake.csv")
j = 20
a1 = Falsex.title
b1 = Falsex.text
print("\n\n",a1[j],"\n\n")
print(str(b1[j]))