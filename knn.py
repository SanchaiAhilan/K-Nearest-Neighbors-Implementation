import pandas as pd
import numpy as np

read = pd.read_csv("vgsales.csv")
readerfull = pd.DataFrame(read)
reader = readerfull.iloc[:,6:11]
reader = np.array(reader)

print("\nEnter Query points :")
NA=float(input(" NA_Sales (0-41.5):\t"))
EU=float(input(" EU_Sales (0-29):\t"))
JP=float(input(" JP_Sales (0-10.2):\t"))
OTHER=float(input(" Other_Sales (0-10.6):\t"))
GLOBAL=float(input(" Global_Sales (0-82.7):\t"))
query = [NA, EU, JP, OTHER, GLOBAL]
choice=int(input("\nSelect Class Label\n (1) Publisher\n (2) Genre\n (3) Platform\n (4) Year\nEnter choice: "))
k=int(input("\nEnter k-value : "))
print("\n")

rows, columns = reader.shape
dist = []
for i in range(rows):
    temp = np.sqrt(np.sum(np.square(query-reader[i])))
    dist.append(temp)

readerfull['Distance'] = dist
readerfull=readerfull.sort_values('Distance', ascending=True)
res=readerfull.iloc[0:k,:]

if choice == 1:
    print(res['Publisher'].value_counts())
elif choice == 2:
    print(res['Genre'].value_counts())
elif choice == 3:
    print(res['Platform'].value_counts())
else:
    print(res['Year'].value_counts())