import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.cbook import get_sample_data
import os
import time


def NDS_3DCRT(data_list, series_name, mode):
    matplotlib.pyplot.switch_backend('Agg')
    path = os.path.split(os.path.realpath(__file__))[0]
    imagePath = path + '/images/case1.png'
    image2Path = path + '/images/case2.png'
    image3Path = path + '/images/case3.png'
    image4Path = path + '/images/case4.png'
    RNS_path = path + '/images/RNS.png'
    Series_names = []

    if mode == "history":
        Series_names.append("All Data")
        for name in series_name:
            Series_names.append(name)
    else:
        for name in series_name:
            Series_names.append(name)
    # adjust canvas size
    plt.figure(figsize=(7.4, 4.8))

    # plot series
    Data_Series = []
    for series in data_list:
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
        if mode == "history":
            Data_Series.append(plt.scatter(x, y, s=4, c="#454545", zorder=5))
            mode = "others"
        else:
            Data_Series.append(plt.scatter(x, y, s=4, zorder=5))

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

    # set white margins
    plt.subplots_adjust(left=0.08, right=0.83, bottom=0.4, top=0.9)

    # set legend
    plt.legend(Data_Series, Series_names, loc='best', bbox_to_anchor=(1.22, 1), prop={'size': 6})
    # plt.legend(Data_Series, Series_names, loc=0)
    # add split lines
    plt.axvline(x=12, c="black", linewidth=0.4)
    plt.axvline(x=32, c="black", linewidth=0.4)
    plt.axvline(x=48.25, c="black", linewidth=0.4)
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


def NDS_IMRT(df):
    matplotlib.pyplot.switch_backend('Agg')
    path = os.path.split(os.path.realpath(__file__))[0]
    x = df["x"].values.tolist()
    y = df["y"].values.tolist()
    print(x)
    print(y)
    plt.scatter(x, y, s=4, c="#454545", zorder=5)
    # set axis
    xlabel_pos = [4, 21, 38, 55, 72, 89]
    plt.xticks(xlabel_pos, ('case 6', 'case 7', 'case 8', 'case 6', 'case 7', 'case 8'), fontsize=8)
    plt.yticks(fontsize=7)
    plt.ylim(-0.1, 0.1)
    plt.title("3DCRT Results", fontsize=7, fontweight="bold")
    plt.suptitle("where is subtitle?", fontsize=10)

    # add green background
    ax1 = plt.gca()
    ax1.axhspan(-0.03, 0.03, facecolor="#C5E1A5", alpha=1, zorder=2)
    ax1.axhspan(-0.05, 0.05, facecolor="#F1F8E9", alpha=1, zorder=1)

    ax1.spines["top"].set_edgecolor("white")
    ax1.spines["bottom"].set_edgecolor("white")
    ax1.spines["right"].set_edgecolor("white")

    # add line
    plt.axvline(x=17, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=34, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=51, c="black", linewidth=0.4)
    plt.axvline(x=68, c="black", linewidth=0.3, linestyle="dashed")
    plt.axvline(x=85, c="black", linewidth=0.3, linestyle="dashed")
    plt.axhline(y=0, c="black", linewidth=0.4)

    plt.savefig("./imrtPP.png", dpi=300)


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


# if __name__ == '__main__':
#     data = {'101106': [float('-0.00840'), float('0.00400')], '110106': [float('-0.02060'), float('-0.00190')],
#             '205106': [float('-0.01770'), float('0.00300')], '208106': [float('-0.00460'), float('0.00470')],
#             '205206': [float('-0.01330'), float('0.00000')], '208206': [float('-0.11110'), float('0.08240')],
#             '205306': [float('0.00760'), float('-0.00600')], '208306': [float('-0.01500'), float('-0.02630')],
#             '303106': [float('-0.00690'), float('-0.00250')], '305106': [float('-0.00390'), float('0.00050')],
#             '403106': [float('0.01010'), float('-0.00150')], '405106': [float('0.01150'), float('0.00230')],
#             '103110': [float('-0.00600'), float('0.00650')], '110110': [float('-0.01600'), float('0.00300')],
#             '303110': [float('-0.00450'), float('0.00000')], '305110': [float('0.00340'), float('0.00340')],
#             '403110': [float('0.00600'), float('-0.01280')], '405110': [float('-0.00430'), float('-0.02740')],
#             '103115': [None, None], '110115': [None, None], '303115': [None, None], '305115': [None, None],
#             '403115': [None, None], '405115': [None, None], '103118': [None, None], '110118': [None, None],
#             '303118': [None, None], '305118': [None, None], '403118': [None, None], '405118': [None, None],
#             '101105': [None, None], '110105': [None, None], '303105': [None, None], '305105': [None, None],
#             '103109': [None, None], '110109': [None, None], '303109': [None, None], '305109': [None, None]}
#     data1 = {'101106': [float('-0.01840'), float('0.01400')], '110106': [float('-0.02060'), float('-0.00290')],
#              '205106': [float('-0.01070'), float('0.01300')], '208106': [float('-0.00460'), float('0.01470')],
#              '205206': [float('-0.01330'), float('0.00100')], '208206': [float('-0.11110'), float('0.08240')],
#              '205306': [float('0.00160'), float('-0.01600')], '208306': [float('-0.01500'), float('-0.01630')],
#              '303106': [float('-0.00190'), float('-0.01250')], '305106': [float('-0.00390'), float('0.01050')],
#              '403106': [float('0.01510'), float('-0.00250')], '405106': [float('0.01150'), float('0.00230')],
#              '103110': [float('-0.00600'), float('0.00150')], '110110': [float('-0.01600'), float('0.00300')],
#              '303110': [float('-0.00150'), float('0.00100')], '305110': [float('0.00340'), float('0.00340')],
#              '403110': [float('0.00300'), float('-0.01780')], '405110': [float('-0.00430'), float('-0.02740')],
#              '103115': [None, None], '110115': [None, None], '303115': [None, None], '305115': [None, None],
#              '403115': [None, None], '405115': [None, None], '103118': [None, None], '110118': [None, None],
#              '303118': [None, None], '305118': [None, None], '403118': [None, None], '405118': [None, None],
#              '101105': [None, None], '110105': [None, None], '303105': [None, None], '305105': [None, None],
#              '103109': [None, None], '110109': [None, None], '303109': [None, None], '305109': [None, None]}
#     data3 = {'101106': [float('-0.01840'), float('0.01400')], '110106': [float('-0.02060'), float('-0.00290')],
#              '205106': [float('-0.01070'), float('0.01300')], '208106': [float('-0.00460'), float('0.01470')],
#              '205206': [float('-0.01330'), float('0.00100')], '208206': [float('-0.11110'), float('0.08240')],
#              '205306': [float('0.00160'), float('-0.01600')], '208306': [float('-0.01500'), float('-0.01630')],
#              '303106': [float('-0.00190'), float('-0.01250')], '305106': [float('-0.00390'), float('0.01050')],
#              '403106': [float('0.01510'), float('-0.00250')], '405106': [float('0.01150'), float('0.00230')],
#              '103110': [float('-0.00600'), float('0.00150')], '110110': [float('-0.01600'), float('0.00300')],
#              '303110': [float('-0.00150'), float('0.00100')], '305110': [float('0.00340'), float('0.00340')],
#              '403110': [float('0.00300'), float('-0.01780')], '405110': [float('-0.00430'), float('-0.02740')],
#              '103115': [None, None], '110115': [None, None], '303115': [None, None], '305115': [None, None],
#              '403115': [None, None], '405115': [None, None], '103118': [None, None], '110118': [None, None],
#              '303118': [None, None], '305118': [None, None], '403118': [None, None], '405118': [None, None],
#              '101105': [None, None], '110105': [None, None], '303105': [None, None], '305105': [None, None],
#              '103109': [None, None], '110109': [None, None], '303109': [None, None], '305109': [None, None]}
#     NDS_3DCRT(data, data1, data3)

if __name__ == '__main__':
    df = pd.read_excel("./imrt.xlsx")
    NDS_IMRT(df)
