import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# load 3DCRT data
df = pd.read_excel("./Book1.xlsx")
print(df)

print(np.unique(df["x-axis"]))

# plot.scatter(x, y, c="color", s=size)
plt.scatter(df["x-axis"], df["a"])
plt.xticks()
plt.show()