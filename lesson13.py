import pandas as pd

produce = ['apples','bannanas','orage','grapes']
prices = [100,200,180,60]

sale_produce = pd.Series(prices,index=produce)
print(sale_produce)

print(sale_produce['grapes'])

total_sales = sale_produce.sum()
print(total_sales)

best_sales=sale_produce.idxmax()
print(f"Best seller is:{best_sales}")


data={'Name':['Nour','Dion','Cait'],
      'Age':[15,17,18],
      'City':['New Jersey','Prishtina','New York']
}

df=pd.DataFrame(data)
print(df)


# df=pd.read_csv(cs.csv)
# df.to_csv("Dion",index = False)
