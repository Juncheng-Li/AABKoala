import json

from rest_framework import status
from rest_framework.response import Response

from apps.graphs import models
from apps.graphs.models import Result, Reading, IMRT, IMRT_misdelivery
from utils import plot


def plot_NDS_3DCRT(self, request):
    results_list = json.loads(request.body.decode('utf-8')).get('results_list')
    mode = json.loads(request.body.decode('utf-8')).get('mode')
    series_name = []
    for resultID in results_list:
        current_results = Result.objects.filter(id=resultID)
        for current_result in current_results:
            series_name.append(current_result.FacilityName)
    print("Series name:")
    print(series_name)
    readings = Reading.objects.filter(result_id__in=results_list)
    data = {"101106": [], "110106": [], "205106": [], "208106": [], "205206": [], "208206": [], "205306": [],
            "208306": [], "303106": [], "305106": [], "403106": [], "405106": [], "103110": [], "110110": [],
            "303110": [], "305110": [], "403110": [], "405110": [], "103115": [], "110115": [], "303115": [],
            "305115": [], "403115": [], "405115": [], "103118": [], "110118": [], "303118": [], "305118": [],
            "403118": [], "405118": [], "101105": [], "110105": [], "303105": [], "305105": [], "103109": [],
            "110109": [], "303109": [], "305109": []}

    for reading in readings:
        for key in data.keys():
            temp = "data[key].append(reading.Reading_" + key + ")"
            exec(temp)

    # If mode is history, load history readings from the DB
    if mode == "history":
        # Load all history readings
        history_readings = Reading.objects.all()

        history_data = {"101106": [], "110106": [], "205106": [], "208106": [], "205206": [], "208206": [],
                        "205306": [],
                        "208306": [], "303106": [], "305106": [], "403106": [], "405106": [], "103110": [],
                        "110110": [],
                        "303110": [], "305110": [], "403110": [], "405110": [], "103115": [], "110115": [],
                        "303115": [],
                        "305115": [], "403115": [], "405115": [], "103118": [], "110118": [], "303118": [],
                        "305118": [],
                        "403118": [], "405118": [], "101105": [], "110105": [], "303105": [], "305105": [],
                        "103109": [],
                        "110109": [], "303109": [], "305109": []}
        for history_reading in history_readings:
            for history_key in history_data.keys():
                tmp = "history_data[history_key].append(history_reading.Reading_" + history_key + ")"
                exec(tmp)
        # Plot with history data
        data_list = [history_data, data]
        graph_info = plot.NDS_3DCRT(data_list, series_name, mode)
    else:
        # Plot without history data
        data_list = [data]
        graph_info = plot.NDS_3DCRT(data_list, series_name, mode)

    graph_obj = models.Graph.objects.create(url=graph_info['url'], fileName=graph_info['fileName'])
    results_obj = models.Result.objects.filter(pk__in=results_list)
    graph_obj.result.add(*results_obj)
    graph_obj.save()
    return Response(graph_info, status=status.HTTP_200_OK)


def plot_NDS_IMRT(self, request):
    facilitys = json.loads(request.body.decode('utf-8')).get('facilitys')
    mode = json.loads(request.body.decode('utf-8')).get('mode')

    data_list = []
    data_format = ["c6_p11_6", "c6_p12_6", "c6_p13_6", "c6_p14_6", "c6_p15_6", "c6_p16_6", "c6_p17_6", "c7_p11_6",
                   "c7_p12_6", "c7_p13_6", "c7_p14_6", "c7_p15_6", "c7_p16_6", "c7_p17_6", "c8_p11_6", "c8_p12_6",
                   "c8_p13_6", "c8_p14_6", "c8_p15_6", "c8_p17_6", "c8_p18_6", "c6_p11_10", "c6_p12_10", "c6_p13_10",
                   "c6_p14_10", "c6_p15_10", "c6_p16_10", "c6_p17_10", "c7_p11_10", "c7_p12_10", "c7_p13_10",
                   "c7_p14_10", "c7_p15_10", "c7_p16_10", "c7_p17_10", "c8_p11_10", "c8_p12_10", "c8_p13_10",
                   "c8_p14_10", "c8_p15_10", "c8_p17_10", "c8_p18_10"]

    all_results = Result.objects.exclude(FacilityName__in=facilitys)
    all_IMRTs = IMRT.objects.filter(result_id__in=all_results)
    all_IMRT_misdeliveries = IMRT_misdelivery.objects.filter(result_id__in=all_results)
    all_data = excludeMisdeliveryData(all_IMRTs, all_IMRT_misdeliveries, data_format)
    data_list.append(all_data)
    # print("all_data: ", all_data)

    for facility in facilitys:
        facility_results = Result.objects.all().filter(FacilityName=facility)
        facility_IMRTs = IMRT.objects.filter(result_id__in=facility_results)
        facility_IMRT_misdeliveries = IMRT_misdelivery.objects.filter(result_id__in=facility_results)
        facility_data = excludeMisdeliveryData(facility_IMRTs, facility_IMRT_misdeliveries, data_format)
        data_list.append(facility_data)
        # print(facility, ":", facility_data)

    # print(data_list)

    if mode == "all":
        series_name = ["All"]
        series_name.extend(facilitys)
        graph_info = plot.NDS_IMRT(data_list, series_name, mode)
        # print(graph_info)

    elif mode == "average":
        series_name = ["All"]
        series_name.extend(facilitys)
        graph_info = plot.NDS_IMRT(averageCalculation(data_list), series_name, mode)
        print(graph_info)

    return Response(status=status.HTTP_200_OK)


def excludeMisdeliveryData(dataset, dataset_misdeliveries, data_format):
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
        print(data)
        avgdata_format = {
            "average1": [], "average2": [], "average3": [], "average4": [], "average5": [], "average6": []
        }
        formatsize = len(data["c6_p11_6"])

        for i in range(formatsize):
            print(i)
            # average1 = np.mean(c6_p11_6, c6_p12_6, c6_p13_6, c6_p15_6, c6_p16_6,c6_p17_6)
            arr1 = [data["c6_p11_6"][i], data["c6_p12_6"][i], data["c6_p13_6"][i], data["c6_p15_6"][i],
                    data["c6_p16_6"][i], data["c6_p17_6"][i]]
            if None in arr1:
                average1 = None
            else:
                average1 = round(sum(arr1)/len(arr1), 3)

            # average2 = np.mean(c7_p11_6, c7_p12_6, c7_p13_6, c7_p15_6, c7_p16_6, c7_p17_6)
            arr2 = [data["c7_p11_6"][i], data["c7_p12_6"][i], data["c7_p13_6"][i], data["c7_p15_6"][i],
                    data["c7_p16_6"][i], data["c6_p17_6"][i]]
            if None in arr2:
                average2 = None
            else:
                average2 = round(sum(arr2)/len(arr2), 3)

            # average3 = np.mean(c8_p11_6, c8_p12_6, c8_p13_6, c8_p15_6, c8_p17_6, c8_p18_6)
            arr3 = [data["c8_p11_6"][i], data["c8_p12_6"][i], data["c8_p13_6"][i], data["c8_p15_6"][i],
                    data["c8_p17_6"][i], data["c8_p18_6"][i]]
            if None in arr3:
                average3 = None
            else:
                average3 = round(sum(arr3)/len(arr3), 3)

            # average4 = np.mean(c6_p11_10, c6_p12_10, c6_p13_10, c6_p15_10, c6_p16_10, c6_p17_10)
            arr4 = [data["c6_p11_10"][i], data["c6_p12_10"][i], data["c6_p13_10"][i], data["c6_p15_10"][i],
                    data["c6_p16_10"][i], data["c6_p17_10"][i]]
            if None in arr4:
                average4 = None
            else:
                average4 = round(sum(arr4)/len(arr4), 3)

            # average5 = np.mean(c7_p11_10, c7_p12_10, c7_p13_10, c7_p15_10, c7_p16_10, c7_p17_10)
            arr5 = [data["c7_p11_10"][i], data["c7_p12_10"][i], data["c7_p13_10"][i], data["c7_p15_10"][i],
                    data["c7_p16_10"][i], data["c7_p17_10"][i]]
            if None in arr5:
                average5 = None
            else:
                average5 = round(sum(arr5)/len(arr5), 3)

            # average6 = np.mean(c8_p11_10, c8_p12_10, c8_p13_10, c8_p15_10, c8_p17_10, c8_p18_10)
            arr6 = [data["c8_p11_10"][i], data["c8_p12_10"][i], data["c8_p13_10"][i], data["c8_p15_10"][i],
                            data["c8_p17_10"][i], data["c8_p18_10"][i]]
            if None in arr6:
                average6 = None
            else:
                average6 = round(sum(arr6)/len(arr6), 3)

            avgdata_format["average1"].append(average1)
            avgdata_format["average2"].append(average2)
            avgdata_format["average3"].append(average3)
            avgdata_format["average4"].append(average4)
            avgdata_format["average5"].append(average5)
            avgdata_format["average6"].append(average6)

        avg_data_list.append(avgdata_format)

    return avg_data_list
