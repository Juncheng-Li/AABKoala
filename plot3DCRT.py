import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from matplotlib.cbook import get_sample_data


def all_data():
    # load 3DCRT data
    df = pd.read_excel("./Book1.xlsx")
    print(df)

    # print(df.groupby(["x-axis"]).count())
    # axis = df["x-axis"].unique()

    # y
    del df["x-axis"]
    # x
    # x = pd.DataFrame({"x": 263 * (1, 2, 3, 4, 5, 6,
    #                               7, 8, 9, 10, 11, 12,
    #                               14, 16.5, 19, 21.5, 24, 26.5,
    #                               28.5, 29.5, 30.5, 31.5, 32.5, 33.5,
    #                               35.5, 36.5, 37.5, 38.5, 39.5, 40.5,
    #                               46, 47, 48, 49,
    #                               53, 54, 55, 56)})
    x = pd.DataFrame({"x": 263 * list(range(1, 39))})
    # xy
    df["x"] = x
    print(df)

    xlabels = np.unique(df["x"])

    # plot.scatter(x, y, c="color", s=size)
    allData = plt.scatter(df["x"], df["a"], s=5, c="#424242", zorder=5)
    plt.xticks(xlabels, ('6', '10', '15', '18', '6FFF', "10FFF",
                         "6", "10", "15", '18', '6FFF', '10FFF',
                         '6', '6', "6", "6", "6", "6",
                         '6', '10', '15', '18', '6FFF', "10FFF",
                         "6", "10", "15", '18', '6FFF', '10FFF',
                         '6', '10', "15", "18",
                         "6", "10", "15", "18"), rotation=90)

    plt.ylim(-0.1, 0.1)
    ax1 = plt.gca()
    ax1.axhspan(-0.03, 0.03, facecolor="#C5E1A5", alpha=1, zorder=2)
    ax1.axhspan(-0.05, 0.05, facecolor="#F1F8E9", alpha=1, zorder=1)
    # ax.set_facecolor("#99FF99")

    plt.legend([allData], ['All Data'])
    plt.savefig("3DCRT.png", dpi=300)
    plt.show()


