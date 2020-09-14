import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")

import pandas as pd
df = pd.read_csv("test.csv")

print("date=",len(df))
print("name=",df.columns.values)
print("index=",df.index.values)

print("mass\n",df["数学"].max())

