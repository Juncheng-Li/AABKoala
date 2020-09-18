import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.cbook import get_sample_data
import os
import time


def NDS_3DCRT(*data):
    path = os.path.split(os.path.realpath(__file__))[0]
    imagePath = path + '/images/case1.png'
    image2Path = path + '/images/case2.png'
    image3Path = path + '/images/case3.png'
    image4Path = path + '/images/case4.png'
    RNS_path = path + '/images/RNS.png'

    # adjust canvas size
    plt.figure(figsize=(7.4, 4.8))

    # plot series
    for series in data:
        x = []
        y = []
        for code in series:
            # flatten measurements in data into list y
            measurements = series[code]
            for measurement in measurements:
                y.append(measurement)
            # flatten code in data into list x
            length = len(measurements)
            for i in range(0, length):
                x.append(code_to_x(code))
        # scatter plot
        # allData = plt.scatter(x, y, s=4, c="#424242", zorder=5)
        allData = plt.scatter(x, y, s=4, zorder=5)

    # set axis
    xlabel_pos = np.unique(x)
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
    plt.subplots_adjust(left=0.08, right=0.83, bottom=0.4, top=0.9)

    # set legend
    plt.legend([allData], ['All Data'], bbox_to_anchor=(1.22, 1))

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

    # add RSN
    RNS_image = plt.imread(get_sample_data(RNS_path))
    RNSax = fig.add_axes([-0.014, 0.403, 0.4, 0.495], anchor='NE', zorder=3)
    RNSax.imshow(RNS_image, alpha=0.65)
    RNSax.axis('off')
    RNS_image = plt.imread(get_sample_data(RNS_path))
    RNSax2 = fig.add_axes([0.068, 0.403, 0.4, 0.495], anchor='NE', zorder=3)
    RNSax2.imshow(RNS_image, alpha=0.65)
    RNSax2.axis('off')

    # plotsave fig
    ticks = time.time()
    ticks = str(round(ticks * 1000))
    plt.savefig(path + "/plGraphs/3DCRT_" + ticks + ".png", dpi=300)
    response = {"fileName": "3DCRT_" + ticks + ".png", "url": path + "/plGraphs/3DCRT_" + ticks + ".png"}
    return response
    # plt.show()


def code_to_x(input_code):
    switcher = {
        "101106": 0,
        "110106": 1,
        "205106": 2,
        "208106": 3,
        "205206": 4,
        "208206": 5,
        "205306": 6,
        "208306": 7,
        "303106": 8,
        "305106": 9,
        "403106": 10,
        "405106": 11,
        "103110": 13,
        "110110": 15.5,
        "303110": 20.5,
        "305110": 23,
        "403110": 27,
        "405110": 30.5,
        "103115": 33.5,
        "110115": 34.5,
        "303115": 35.5,
        "305115": 36.5,
        "403115": 37.5,
        "405115": 38.5,
        "103118": 40.5,
        "110118": 41.5,
        "303118": 42.5,
        "305118": 43.5,
        "403118": 44.5,
        "405118": 45.5,
        "101105": 51,
        "110105": 52,
        "303105": 53,
        "305105": 54,
        "103109": 58,
        "110109": 59,
        "303109": 60,
        "305109": 61
    }
    return switcher.get(input_code)
