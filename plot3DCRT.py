import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from matplotlib.cbook import get_sample_data


def all_data():
    imagePath = '/Users/jcl/Desktop/AABKoala/images/case1full.png'
    image2Path = '/Users/jcl/Desktop/AABKoala/images/case2full.png'
    image3Path = '/Users/jcl/Desktop/AABKoala/images/case3full.png'
    image4Path = '/Users/jcl/Desktop/AABKoala/images/case4full.png'
    all_cases_path = '/Users/jcl/Desktop/AABKoala/images/all_cases.png'
    # load 3DCRT data
    df = pd.read_excel("./Book1.xlsx")
    print(df)

    # print(df.groupby(["x-axis"]).count())
    # axis = df["x-axis"].unique()

    # y
    del df["x-axis"]
    # x-axis pos
    x = pd.DataFrame({"x": 263 * (0, 1, 2, 3, 4, 5,
                                  6, 7, 8, 9, 10, 11,
                                  13, 15.5, 20.5, 23, 27, 30.5,
                                  33.5, 34.5, 35.5, 36.5, 37.5, 38.5,
                                  40.5, 41.5, 42.5, 43.5, 44.5, 45.5,
                                  51, 52, 53, 54,
                                  58, 59, 60, 61)})
    # x = pd.DataFrame({"x": 263 * list(range(1, 39))})
    df["x"] = x
    print(df)

    # adjust canvas size
    # plt.figure(figsize=(8.4, 4.8))
    plt.figure(figsize=(7.4, 4.8))

    # scatter plot
    allData = plt.scatter(df["x"], df["a"], s=4, c="#424242", zorder=5)

    # set axis
    xlabel_pos = np.unique(df["x"])
    plt.xticks(xlabel_pos, ('6', '10', '15', '18', '6FFF', "10FFF",
                            "6", "10", "15", '18', '6FFF', '10FFF',
                            '6', '6', "6", "6", "6", "6",
                            '6', '10', '15', '18', '6FFF', "10FFF",
                            "6", "10", "15", '18', '6FFF', '10FFF',
                            '6', '10', "15", "18",
                            "6", "10", "15", "18"), rotation=90, fontsize=7)
    plt.yticks(fontsize=7)
    plt.ylim(-0.1, 0.1)
    plt.title("3DCRT Results", fontsize=7, fontweight="bold")

    # add green background
    ax1 = plt.gca()
    ax1.axhspan(-0.03, 0.03, facecolor="#C5E1A5", alpha=1, zorder=2)
    ax1.axhspan(-0.05, 0.05, facecolor="#F1F8E9", alpha=1, zorder=1)
    # ax.set_facecolor("#99FF99")

    # set white margins
    plt.subplots_adjust(left=0.08, right=0.83, bottom=0.4)

    # set legend
    plt.legend([allData], ['All Data'], bbox_to_anchor=(1.2, 1))

    # add split lines
    plt.axvline(x=12, c="black", linewidth=0.4)
    plt.axvline(x=32, c="black", linewidth=0.4)
    plt.axvline(x=48.25, c="black", linewidth=0.4)
    plt.axvline(x=5.5, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=39.5, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=56, c="black", linewidth=0.3, linestyle="dashed")
    plt.axhline(y=0, c="black", linewidth=0.4)

    # add images
    fig = plt.gcf()
    case_image = plt.imread(get_sample_data(imagePath))
    image1ax = fig.add_axes([0.015, 0.067, 0.24, 0.24], anchor='NE', zorder=3)
    image1ax.imshow(case_image)
    image1ax.axis('off')
    case_image = plt.imread(get_sample_data(image2Path))
    image2ax = fig.add_axes([0.23, 0.065, 0.24, 0.24], anchor='NE', zorder=3)
    image2ax.imshow(case_image)
    image2ax.axis('off')
    case_image = plt.imread(get_sample_data(image3Path))
    image3ax = fig.add_axes([0.415, 0.065, 0.24, 0.24], anchor='NE', zorder=2)
    image3ax.imshow(case_image)
    image3ax.axis('off')
    case_image = plt.imread(get_sample_data(image4Path))
    image4ax = fig.add_axes([0.603, 0.065, 0.24, 0.24], anchor='NE', zorder=3)
    image4ax.imshow(case_image)
    image4ax.axis('off')

    # save fig
    plt.savefig("3DCRT.png", dpi=300)
    # plt.show()
