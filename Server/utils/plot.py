import os
import random
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data


def NDS_3DCRT(series_data, series_name, mode):
    # allow matplotlib to plot at background
    matplotlib.pyplot.switch_backend('Agg')
    path = os.path.split(os.path.realpath(__file__))[0]
    imagePath = path + '/images/case1.png'
    image2Path = path + '/images/case2.png'
    image3Path = path + '/images/case3.png'
    image4Path = path + '/images/case4.png'
    RNS_path = path + '/images/RNS.png'
    Series_names = []

    if mode == "all":
        Series_names.append("All Data")
        for name in series_name:
            Series_names.append(name)
    else:
        for name in series_name:
            Series_names.append(name)
    # adjust canvas size
    plt.figure(figsize=(7.4, 4.8))

    # plot series
    plot_series = []
    for i in range(0, len(series_data)):
        series = series_data[i]
        s_name = series_name[i]
        x = []
        y = []
        for code in series:
            # flatten measurements in data into a list of y value
            measurements = series[code]
            for measurement in measurements:
                y.append(measurement)
            # flatten code in data into list x
            length = len(measurements)
            for k in range(0, length):
                x.append(code_to_x_3dcrt(code))
        # scatter plot
        if s_name == "All":
            # plot "All data" data points in black
            plot_series.append(plt.scatter(x, y, s=3.7, c="#454545", zorder=5))
        else:
            # plot other facility data points in random colors
            plot_series.append(plt.scatter(x, y, s=3.7, c=get_color(i), zorder=5))

    # set axis
    xlabel_pos = np.unique(x)
    plt.xticks(xlabel_pos, ('6', '10', '15', '18', '6FFF', "10FFF",
                            "6", "10", "15", '18', '6FFF', '10FFF',
                            '6', '6', "6", "6", "6", "6",
                            '6', '10', '15', '18', '6FFF', "10FFF",
                            "6", "10", "15", '18', '6FFF', '10FFF',
                            '6', '10', "15", "18",
                            "6", "10", "15", "18"), rotation=90, fontsize=7)
    plt.xlim(-1, 65)
    plt.yticks(fontsize=7)
    plt.ylim(-0.1, 0.1)
    plt.title("3DCRT Results", fontsize=7, fontweight="bold")

    # add green background
    ax = plt.gca()
    ax.axhspan(-0.03, 0.03, facecolor="#C5E1A5", alpha=1, zorder=2)
    ax.axhspan(-0.05, 0.05, facecolor="#F1F8E9", alpha=1, zorder=1)

    # set white margins
    plt.subplots_adjust(left=0.08, right=0.83, bottom=0.4, top=0.9)

    # set legend
    plt.legend(plot_series, Series_names, loc='best', bbox_to_anchor=(1.22, 1), prop={'size': 6})

    # add split lines
    plt.axvline(x=12, c="black", linewidth=0.4)
    plt.axvline(x=32, c="black", linewidth=0.4)
    plt.axvline(x=47, c="black", linewidth=0.4)
    plt.axvline(x=5.5, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=39.5, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=56, c="black", linewidth=0.3, linestyle="dashed")
    plt.axhline(y=0, c="black", linewidth=0.4)

    # add case images
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
    RNSax = fig.add_axes([-0.035, 0.403, 0.4, 0.495], anchor='NE', zorder=3)
    RNSax.imshow(RNS_image, alpha=0.65)
    RNSax.axis('off')
    RNS_image = plt.imread(get_sample_data(RNS_path))
    RNSax2 = fig.add_axes([0.05, 0.403, 0.4, 0.495], anchor='NE', zorder=3)
    RNSax2.imshow(RNS_image, alpha=0.65)
    RNSax2.axis('off')

    # plot fig
    ticks = time.time()
    ticks = str(round(ticks * 1000))
    plt.savefig(path + "/plGraphs/3DCRT_" + ticks + ".png", dpi=300)
    response = {"fileName": "3DCRT_" + ticks + ".png", "url": path + "/plGraphs/3DCRT_" + ticks + ".png"}
    return response


def NDS_IMRT(series_data, series_name, mode):
    # allow matplotlib to plot at background
    matplotlib.pyplot.switch_backend('Agg')
    path = os.path.split(os.path.realpath(__file__))[0]

    # plot
    plot_series = []
    for i in range(0, len(series_data)):
        series = series_data[i]
        s_name = series_name[i]
        x = []
        y = []
        for code in series:
            # flatten measurements in data into list y
            measurements = series[code]
            for measurement in measurements:
                y.append(measurement)
            # flatten code in data into list x
            length = len(measurements)
            for k in range(0, length):
                if mode == "all":
                    x.append(code_to_x_imrt(code))
                elif mode == "average":
                    x.append(avg_to_x(code))
                elif mode == "std":
                    x.append(std_to_x(code))
        # scatter plot
        if s_name == "All":
            plot_series.append(plt.scatter(x, y, s=4, c="#454545", zorder=5))
        else:
            plot_series.append(plt.scatter(x, y, s=4, c=get_color(i), zorder=5))

    # set axis
    xlabel_pos = [8, 25, 42, 59, 76, 93]
    plt.xticks(xlabel_pos, ('case 6', 'case 7', 'case 8', 'case 6', 'case 7', 'case 8'), fontsize=6)
    plt.xlim(0, 102)
    plt.yticks(fontsize=6)
    plt.ylim(-0.1, 0.1)

    # set white margins
    plt.subplots_adjust(bottom=0.13)

    # add green/grey background
    ax = plt.gca()
    if mode == "all":
        ax.axhspan(-0.03, 0.03, facecolor="#C5E1A5", alpha=1, zorder=2)
        ax.axhspan(-0.05, 0.05, facecolor="#F1F8E9", alpha=1, zorder=1)
    else:
        ax.axhspan(-0.03, 0.03, facecolor="#BABAAB", alpha=1, zorder=2)
        ax.axhspan(-0.05, 0.05, facecolor="#E8E8E3", alpha=1, zorder=1)

    # configure plot boundaries
    ax.spines["top"].set_edgecolor("white")
    ax.spines["bottom"].set_edgecolor("white")
    ax.spines["right"].set_edgecolor("white")
    ax.tick_params(bottom=False)

    # set title and sub title
    ax.set_title('IMRT Results', y=1.1, horizontalalignment='center', pad=-4, size=10, fontweight='bold')
    if mode == 'all':
        plt.suptitle("All in-volume points", y=0.93, x=0.51, fontsize=8)
    elif mode == 'average':
        plt.suptitle("Average of in-volume points", y=0.93, x=0.51, fontsize=8)
    elif mode == 'std':
        plt.suptitle("Standard Deviation of in-volume points", y=0.93, x=0.51, fontsize=8)

    # add line
    plt.axvline(x=17, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=34, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=51, c="black", linewidth=0.4)
    plt.axvline(x=68, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=85, c="black", linewidth=0.3, linestyle="dashed")
    plt.axhline(y=0, c="black", linewidth=0.4)

    # add energy text
    plt.text(23, -0.119, "6X", fontsize=6, zorder=6)
    plt.text(74, -0.119, "10X", fontsize=6, zorder=6)

    # add legend
    ax.legend(plot_series, series_name, loc='center', bbox_to_anchor=(0.5, -0.135), ncol=len(series_name), fontsize=8,
               frameon=False)

    # save plot
    ticks = time.time()
    ticks = str(round(ticks * 1000))
    plt.savefig(path + "/plGraphs/IMRT_" + mode + "_" + ticks + ".png", dpi=300)
    response = {"fileName": "IMRT_" + mode + "_" + ticks + ".png", "url": path + "/plGraphs/IMRT_" + mode + "_" + ticks + ".png"}
    return response


def code_to_x_3dcrt(input_code):
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


def code_to_x_imrt(input_code):
    switcher = {
        "c6_p11_6": 1,
        "c6_p12_6": 2,
        "c6_p13_6": 3,
        "c6_p14_6": None,
        "c6_p15_6": 5,
        "c6_p16_6": 6,
        "c6_p17_6": 7,
        "c7_p11_6": 18,
        "c7_p12_6": 19,
        "c7_p13_6": 20,
        "c7_p14_6": None,
        "c7_p15_6": 22,
        "c7_p16_6": 23,
        "c7_p17_6": 24,
        "c8_p11_6": 35,
        "c8_p12_6": 36,
        "c8_p13_6": 37,
        "c8_p14_6": None,
        "c8_p15_6": 39,
        "c8_p17_6": 40,
        "c8_p18_6": 41,
        "c6_p11_10": 52,
        "c6_p12_10": 53,
        "c6_p13_10": 54,
        "c6_p14_10": None,
        "c6_p15_10": 56,
        "c6_p16_10": 57,
        "c6_p17_10": 58,
        "c7_p11_10": 69,
        "c7_p12_10": 70,
        "c7_p13_10": 71,
        "c7_p14_10": None,
        "c7_p15_10": 73,
        "c7_p16_10": 74,
        "c7_p17_10": 75,
        "c8_p11_10": 86,
        "c8_p12_10": 87,
        "c8_p13_10": 88,
        "c8_p14_10": None,
        "c8_p15_10": 90,
        "c8_p17_10": 91,
        "c8_p18_10": 92,
    }
    return switcher.get(input_code)


def avg_to_x(input_code):
    switcher = {
        "average1": 4,
        "average2": 21,
        "average3": 38,
        "average4": 55,
        "average5": 72,
        "average6": 89,
    }
    return switcher.get(input_code)


def std_to_x(input_code):
    switcher = {
        "average1": 4,
        "average2": 21,
        "average3": 38,
        "average4": 55,
        "average5": 72,
        "average6": 89,
    }
    return switcher.get(input_code)


def get_color(i):
    color_list = ["#454545", "#FF2A00", "#FFD500", "#00CCAA", "#CC8800", "#9933FF", "#0066CC"]
    if i > len(color_list):
        rgb = (random.random(), random.random(), random.random())
        return rgb
    return color_list[i]
