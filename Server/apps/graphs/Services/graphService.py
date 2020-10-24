import json

import numpy as np
from rest_framework import status
from rest_framework.response import Response

from apps.graphs import models
from apps.graphs.models import Result, Nds_3dcrt, Nds_imrt, Nds_imrt_misdelivery, Nds_3dcrt_misdelivery
from utils import plot


def plot_NDS_3DCRT(self, request):
    facilitys = json.loads(request.body.decode('utf-8')).get('facilitys')
    mode = json.loads(request.body.decode('utf-8')).get('mode')

    data_list = []
    facilitys_id_list = []
    data_format = ["code_101106", "code_110106", "code_205106", "code_208106", "code_205206", "code_208206",
                   "code_205306", "code_208306", "code_303106", "code_305106", "code_403106", "code_405106",
                   "code_103110", "code_110110", "code_303110", "code_305110", "code_403110", "code_405110",
                   "code_103115", "code_110115", "code_303115", "code_305115", "code_403115", "code_405115",
                   "code_103118", "code_110118", "code_303118", "code_305118", "code_403118", "code_405118",
                   "code_101105", "code_110105", "code_303105", "code_305105", "code_103109", "code_110109",
                   "code_303109", "code_305109"]

    for value in facilitys.values():
        facilitys_id_list.extend(value)

    all_results = Result.objects.exclude(pk__in=facilitys_id_list)
    all_Nds_3dcrts = Nds_3dcrt.objects.filter(result_id__in=all_results)
    all_Nds_3dcrt_misdeliveries = Nds_3dcrt_misdelivery.objects.filter(result_id__in=all_results)
    all_data = excludeMisdeliveryData(all_Nds_3dcrts, all_Nds_3dcrt_misdeliveries, data_format, "NDS_3DCRT")
    data_list.append(all_data)

    for facility in facilitys.keys():
        facility_results = Result.objects.all().filter(pk__in=facilitys[facility])
        facility_Nds_3dcrts = Nds_3dcrt.objects.filter(result_id__in=facility_results)
        facility_Nds_3dcrt_misdeliveries = Nds_3dcrt_misdelivery.objects.filter(result_id__in=facility_results)
        facility_data = excludeMisdeliveryData(facility_Nds_3dcrts, facility_Nds_3dcrt_misdeliveries, data_format, "NDS_3DCRT")
        data_list.append(facility_data)

    if mode == "all":
        series_name = ["All"]
        series_name.extend(facilitys.keys())
        graph_info = plot.NDS_3DCRT(data_list, series_name, mode)

    graph_obj = models.Graph.objects.create(url=graph_info['url'], fileName=graph_info['fileName'])
    facility_results = Result.objects.all().filter(pk__in=facilitys_id_list)
    graph_obj.result.add(*facility_results)
    graph_obj.save()
    return Response(graph_info, status=status.HTTP_200_OK)


def plot_NDS_IMRT(self, request):
    facilitys = json.loads(request.body.decode('utf-8')).get('facilitys')
    mode = json.loads(request.body.decode('utf-8')).get('mode')

    data_list = []
    facilitys_id_list = []
    data_format = ["code_c6_p11_6", "code_c6_p12_6", "code_c6_p13_6", "code_c6_p14_6", "code_c6_p15_6",
                   "code_c6_p16_6", "code_c6_p17_6", "code_c7_p11_6", "code_c7_p12_6", "code_c7_p13_6",
                   "code_c7_p14_6", "code_c7_p15_6", "code_c7_p16_6", "code_c7_p17_6", "code_c8_p11_6", "code_c8_p12_6",
                   "code_c8_p13_6", "code_c8_p14_6", "code_c8_p15_6", "code_c8_p17_6", "code_c8_p18_6",
                   "code_c6_p11_10", "code_c6_p12_10", "code_c6_p13_10", "code_c6_p14_10", "code_c6_p15_10",
                   "code_c6_p16_10", "code_c6_p17_10", "code_c7_p11_10", "code_c7_p12_10", "code_c7_p13_10",
                   "code_c7_p14_10", "code_c7_p15_10", "code_c7_p16_10", "code_c7_p17_10", "code_c8_p11_10",
                   "code_c8_p12_10", "code_c8_p13_10", "code_c8_p14_10", "code_c8_p15_10", "code_c8_p17_10",
                   "code_c8_p18_10"]

    for value in facilitys.values():
        facilitys_id_list.extend(value)

    all_results = Result.objects.exclude(pk__in=facilitys_id_list)
    all_IMRTs = Nds_imrt.objects.filter(result_id__in=all_results)
    all_Nds_imrt_misdeliveries = Nds_imrt_misdelivery.objects.filter(result_id__in=all_results)
    all_data = excludeMisdeliveryData(all_IMRTs, all_Nds_imrt_misdeliveries, data_format, "NDS_IMRT")
    data_list.append(all_data)

    for facility in facilitys.keys():
        facility_results = Result.objects.all().filter(pk__in=facilitys[facility])
        facility_Nds_imrts = Nds_imrt.objects.filter(result_id__in=facility_results)
        facility_Nds_imrt_misdeliveries = Nds_imrt_misdelivery.objects.filter(result_id__in=facility_results)
        facility_data = excludeMisdeliveryData(facility_Nds_imrts, facility_Nds_imrt_misdeliveries, data_format, "NDS_IMRT")
        data_list.append(facility_data)

    if mode == "all":
        series_name = ["All"]
        series_name.extend(facilitys.keys())
        graph_info = plot.NDS_IMRT(data_list, series_name, mode)

    elif mode == "average":
        series_name = ["All"]
        series_name.extend(facilitys.keys())
        graph_info = plot.NDS_IMRT(averageCalculation(data_list), series_name, mode)

    elif mode == "std":
        series_name = ["All"]
        series_name.extend(facilitys.keys())
        graph_info = plot.NDS_IMRT(standardDeviationCalculation(data_list), series_name, mode)

    graph_obj = models.Graph.objects.create(url=graph_info['url'], fileName=graph_info['fileName'])
    facility_results = Result.objects.all().filter(pk__in=facilitys_id_list)
    graph_obj.result.add(*facility_results)
    graph_obj.save()
    return Response(graph_info, status=status.HTTP_200_OK)


def excludeMisdeliveryData(dataset, dataset_misdeliveries, data_format, graphType):
    data_dict = dict([(k, []) for k in data_format])
    for data in dataset:
        dataset_misdelivery = dataset_misdeliveries.filter(result_id=data.result_id)
        misdelivery = dataset_misdelivery[0]

        for key in data_dict.keys():
            temp = """
if misdelivery.""" + key + """ == 1:
    data_dict[\"""" + key + """\"].append(None)
else:
    data_dict[\"""" + key + """\"].append(data.""" + key + """)
            """
            exec(temp)

    return data_dict


def averageCalculation(data_list):
    avg_data_list = []

    for data in data_list:
        avgdata_format = {
            "average1": [], "average2": [], "average3": [], "average4": [], "average5": [], "average6": []
        }
        formatsize = len(data["code_c6_p11_6"])

        for i in range(formatsize):
            # average1 = np.mean(c6_p11_6, c6_p12_6, c6_p13_6, c6_p15_6, c6_p16_6,c6_p17_6)
            arr1 = [data["code_c6_p11_6"][i], data["code_c6_p12_6"][i], data["code_c6_p13_6"][i], data["code_c6_p15_6"][i],
                    data["code_c6_p16_6"][i], data["code_c6_p17_6"][i]]
            if None in arr1:
                average1 = None
            else:
                average1 = round(sum(arr1) / len(arr1), 3)

            # average2 = np.mean(c7_p11_6, c7_p12_6, c7_p13_6, c7_p15_6, c7_p16_6, c7_p17_6)
            arr2 = [data["code_c7_p11_6"][i], data["code_c7_p12_6"][i], data["code_c7_p13_6"][i], data["code_c7_p15_6"][i],
                    data["code_c7_p16_6"][i], data["code_c6_p17_6"][i]]
            if None in arr2:
                average2 = None
            else:
                average2 = round(sum(arr2) / len(arr2), 3)

            # average3 = np.mean(c8_p11_6, c8_p12_6, c8_p13_6, c8_p15_6, c8_p17_6, c8_p18_6)
            arr3 = [data["code_c8_p11_6"][i], data["code_c8_p12_6"][i], data["code_c8_p13_6"][i], data["code_c8_p15_6"][i],
                    data["code_c8_p17_6"][i], data["code_c8_p18_6"][i]]
            if None in arr3:
                average3 = None
            else:
                average3 = round(sum(arr3) / len(arr3), 3)

            # average4 = np.mean(c6_p11_10, c6_p12_10, c6_p13_10, c6_p15_10, c6_p16_10, c6_p17_10)
            arr4 = [data["code_c6_p11_10"][i], data["code_c6_p12_10"][i], data["code_c6_p13_10"][i], data["code_c6_p15_10"][i],
                    data["code_c6_p16_10"][i], data["code_c6_p17_10"][i]]
            if None in arr4:
                average4 = None
            else:
                average4 = round(sum(arr4) / len(arr4), 3)

            # average5 = np.mean(c7_p11_10, c7_p12_10, c7_p13_10, c7_p15_10, c7_p16_10, c7_p17_10)
            arr5 = [data["code_c7_p11_10"][i], data["code_c7_p12_10"][i], data["code_c7_p13_10"][i], data["code_c7_p15_10"][i],
                    data["code_c7_p16_10"][i], data["code_c7_p17_10"][i]]
            if None in arr5:
                average5 = None
            else:
                average5 = round(sum(arr5) / len(arr5), 3)

            # average6 = np.mean(c8_p11_10, c8_p12_10, c8_p13_10, c8_p15_10, c8_p17_10, c8_p18_10)
            arr6 = [data["code_c8_p11_10"][i], data["code_c8_p12_10"][i], data["code_c8_p13_10"][i], data["code_c8_p15_10"][i],
                    data["code_c8_p17_10"][i], data["code_c8_p18_10"][i]]
            if None in arr6:
                average6 = None
            else:
                average6 = round(sum(arr6) / len(arr6), 3)

            avgdata_format["average1"].append(average1)
            avgdata_format["average2"].append(average2)
            avgdata_format["average3"].append(average3)
            avgdata_format["average4"].append(average4)
            avgdata_format["average5"].append(average5)
            avgdata_format["average6"].append(average6)

        avg_data_list.append(avgdata_format)

    return avg_data_list


def standardDeviationCalculation(data_list):
    std_data_list = []

    for data in data_list:
        avgdata_format = {
            "std1": [], "std2": [], "std3": [], "std4": [], "std5": [], "std6": []
        }
        formatsize = len(data["code_c6_p11_6"])

        for i in range(formatsize):
            # std1 = std (c6_p11_6，c6_p12_6， c6_p13_6，  c6_p15_6， c6_p16_6，c6_p17_6)
            std1_arr = [data["code_c6_p11_6"][i], data["code_c6_p12_6"][i], data["code_c6_p13_6"][i], data["code_c6_p15_6"][i],
                        data["code_c6_p16_6"][i], data["code_c6_p17_6"][i]]
            if None in std1_arr:
                std1 = None
            else:
                std1 = np.std(std1_arr, ddof=1)

            # std2 = std（c7_p11_6， c7_p12_6， c7_p13_6，  c7_p15_6， c7_p16_6， c7_p17_6）
            std2_arr = [data["code_c7_p11_6"][i], data["code_c7_p12_6"][i], data["code_c7_p13_6"][i], data["code_c7_p15_6"][i],
                        data["code_c7_p16_6"][i], data["code_c6_p17_6"][i]]
            if None in std2_arr:
                std2 = None
            else:
                std2 = np.std(std2_arr, ddof=1)

            # std3 = std（c8_p11_6，c8_p12_6， c8_p13_6，  c8_p15_6， c8_p17_6， c8_p18_6）
            std3_arr = [data["code_c8_p11_6"][i], data["code_c8_p12_6"][i], data["code_c8_p13_6"][i], data["code_c8_p15_6"][i],
                        data["code_c8_p17_6"][i], data["code_c8_p18_6"][i]]
            if None in std3_arr:
                std3 = None
            else:
                std3 = np.std(std3_arr, ddof=1)

            # std4 = std（c6_p11_10， c6_p12_10， c6_p13_10， c6_p15_10， c6_p16_10， c6_p17_10）
            std4_arr = [data["code_c6_p11_10"][i], data["code_c6_p12_10"][i], data["code_c6_p13_10"][i], data["code_c6_p15_10"][i],
                        data["code_c6_p16_10"][i], data["code_c6_p17_10"][i]]
            if None in std4_arr:
                std4 = None
            else:
                std4 = np.std(std4_arr, ddof=1)

            # std5 = std（c7_p11_10， c7_p12_10， c7_p13_10， c7_p15_10， c7_p16_10， c7_p17_10
            std5_arr = [data["code_c7_p11_10"][i], data["code_c7_p12_10"][i], data["code_c7_p13_10"][i], data["code_c7_p15_10"][i],
                        data["code_c7_p16_10"][i], data["code_c7_p17_10"][i]]
            if None in std5_arr:
                std5 = None
            else:
                std5 = np.std(std5_arr, ddof=1)

            # std6 = std（c8_p11_10，c8_p12_10， c8_p13_10，  c8_p15_10， c8_p17_10， c8_p18_10）
            std6_arr = [data["code_c8_p11_10"][i], data["code_c8_p12_10"][i], data["code_c8_p13_10"][i], data["code_c8_p15_10"][i],
                        data["code_c8_p17_10"][i], data["code_c8_p18_10"][i]]
            if None in std6_arr:
                std6 = None
            else:
                std6 = np.std(std6_arr, ddof=1)

            avgdata_format["std1"].append(std1)
            avgdata_format["std2"].append(std2)
            avgdata_format["std3"].append(std3)
            avgdata_format["std4"].append(std4)
            avgdata_format["std5"].append(std5)
            avgdata_format["std6"].append(std6)

        std_data_list.append(avgdata_format)

    return std_data_list
