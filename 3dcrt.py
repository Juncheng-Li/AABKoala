import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# load 3DCRT data
df = pd.read_excel("./Book1.xlsx")
print(df)

# print(df.groupby(["x-axis"]).count())
# axis = df["x-axis"].unique()


# y
del df["x-axis"]
# x
x = pd.DataFrame({"x": 263 * list(range(1, 39))})
# xy
df["x"] = x
print(df)

xlabels = np.unique(df["x"])

# plot.scatter(x, y, c="color", s=size)
plt.scatter(df["x"], df["a"])
plt.xticks(xlabels, ('6', '10', '15', '18', '6FFF', "10FFF",
                     "6", "10", "15", '18', '6FFF', '10FFF',
                     '6', '6', "6", "6", "6", "6",
                     '6', '10', '15', '18', '6FFF', "10FFF",
                     "6", "10", "15", '18', '6FFF', '10FFF',
                     '6', '10', "15", "18",
                     "6", "10", "15", "18"), rotation=90)
plt.ylim(-0.1, 0.1)
plt.show()
