import pandas as pd
homeno=int(input("enter the home no:"))
homename=input("enter home name:")
place=input("enter place:")
sqfeet=int(input("enter square feet:"))
price=int(input("enter the price:"))
d={"homeno":[homeno,1,2],"homename":[homename,"sh","jk"],"place":[place,"chakkai","soul"],"squarefeet":[sqfeet,7,8],"price":[price,9,10]}
print(d)
df=pd.DataFrame(d)
print(df)
df.to_excel("sample.xlsx")
df.to_csv("sample.csv")