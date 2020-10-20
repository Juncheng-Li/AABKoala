import pandas as pd
import json
import http.client
import mimetypes
from pandas import json_normalize
from LocalProgram.config import *
from datetime import datetime
import time
import math


class resultRequest:

    def __init__(self):
        self.authorization = authorization
        self.host = host
        self.port = port
        self.conn = http.client.HTTPConnection(self.host, self.port)

    def parseExcel(self):
        filename = "upload/uploadingData.xlsx"
        df = pd.read_excel(filename)
        df["AuditDate"] = pd.to_datetime(df["AuditDate"], errors='coerce')
        df["AuditDate"] = df["AuditDate"].dt.strftime("%Y-%m-%d")
        resultList = []
        ids = []
        roundIndex = ['Reading_101106', 'Reading_110106', 'Reading_205106', 'Reading_208106', 'Reading_205206',
                      'Reading_208206', 'Reading_205306', 'Reading_208306', 'Reading_303106', 'Reading_305106',
                      'Reading_403106', 'Reading_405106', 'Reading_103110', 'Reading_110110', 'Reading_303110',
                      'Reading_305110', 'Reading_403110', 'Reading_405110', 'Reading_103115', 'Reading_110115',
                      'Reading_303115', 'Reading_305115', 'Reading_403115', 'Reading_405115', 'Reading_103118',
                      'Reading_110118', 'Reading_303118', 'Reading_305118', 'Reading_403118', 'Reading_405118',
                      'Reading_101105', 'Reading_110105', 'Reading_303105', 'Reading_305105', 'Reading_103109',
                      'Reading_110109', 'Reading_303109', 'Reading_305109', 'c6_p11_6', 'c6_p12_6', 'c6_p13_6',
                      'c6_p14_6', 'c6_p15_6', 'c6_p16_6', 'c6_p17_6', 'c7_p11_6', 'c7_p12_6', 'c7_p13_6', 'c7_p14_6',
                      'c7_p15_6', 'c7_p16_6', 'c7_p17_6', 'c8_p11_6', 'c8_p12_6', 'c8_p13_6', 'c8_p14_6', 'c8_p15_6',
                      'c8_p17_6', 'c8_p18_6', 'c6_p11_10', 'c6_p12_10', 'c6_p13_10', 'c6_p14_10', 'c6_p15_10',
                      'c6_p16_10', 'c6_p17_10', 'c7_p11_10', 'c7_p12_10', 'c7_p13_10', 'c7_p14_10', 'c7_p15_10',
                      'c7_p16_10', 'c7_p17_10', 'c8_p11_10', 'c8_p12_10', 'c8_p13_10', 'c8_p14_10', 'c8_p15_10',
                      'c8_p17_10', 'c8_p18_10', 'fac_6', 'fac_10', 'fac_15', 'fac_18', 'fac_6FFF', 'fac_10FFF', 'TPR_6',
                      'TPR_10', 'TPR_15', 'TPR_18', 'TPR_6FFF', 'TPR_10FFF', ]
        decimals = pd.Series([4 for _ in range(92)], index=roundIndex)
        df = df.round(decimals)

        for i in range(len(df)):
            id = df.loc[i, 'id']
            if not math.isnan(id):
                ids.append(str(int(id)))
            unested = df.loc[i, "AuditID":"Phantom"].to_json()
            facilityOutput = df.loc[i, "fac_6":"fac_10FFF"].to_json().replace("fac", "energy")
            tpr = df.loc[i, "TPR_6":"TPR_10FFF"].to_json().replace("TPR", "energy")
            readings = df.loc[i, "Reading_101106":"Reading_305109"].to_json()
            misdelivery = df.loc[i, "Misdelivery_101106":"Misdelivery_305109"].to_json()
            imrt = df.loc[i, "c6_p11_6":"c8_p18_10"].to_json()
            imrt_misdelivery = df.loc[i, "imrt_misdelivery_c6_p11_6":"imrt_misdelivery_c8_p18_10"].to_json().replace(
                "imrt_misdelivery_", "")

            result = json.loads(unested)
            result.update({"facilityOutput": [json.loads(facilityOutput)]})
            result.update({"TPR": [json.loads(tpr)]})
            result.update({"Reading": [json.loads(readings)]})
            result.update({"Misdelivery": [json.loads(misdelivery)]})
            result.update({"IMRT": [json.loads(imrt)]})
            result.update({"IMRT_misdelivery": [json.loads(imrt_misdelivery)]})
            resultList.append(json.dumps(result))
            # print("resultList in Excel")
            # print(resultList)

        return (resultList, ids)

    def insertNewResult(self):
        resultsList = self.parseExcel()[0]
        if len(resultsList) == 1:
            payload = resultsList[0]
            headers = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
            }
            time1 = time.time()
            self.conn.request("POST", "/graphs/results/", payload, headers)
            # payload is HTTP content
            res = self.conn.getresponse()
            print(res.status, res.reason)
            time2 = time.time()
            data = res.read()
            print("insert request completed, takes time %d" % (time2 - time1) + " seconds")
            print("Single results insertNewResult")
            print(data.decode("utf-8"))
            return res
        else:
            # when there are multiple results to be inserted, use this one instead
            payload = []
            for result in resultsList:
                payload.append(json.loads(result))
            payload = json.dumps(payload)
            headers = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
            }
            time1 = time.time()
            self.conn.request("POST", "/graphs/resultsList/", payload, headers)
            res = self.conn.getresponse()
            print(res.status, res.reason)
            time2 = time.time()
            data = res.read()
            print("insert request completed, takes time %d" % (time2 - time1) + " seconds")
            print("Multiple results insertNewResult")
            print(data.decode("utf-8"))
            return res

    # list all date in the database
    def listResults(self):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        print("downloading the whole dataset...")
        self.conn.request("GET", "/graphs/results/", payload, headers)
        res = self.conn.getresponse()
        # print("listResults: res.status, res.reason")
        # print(res.status, res.reason)
        data = res.read()
        content = bytes.decode(data, 'utf-8')
        contentInJson = json.loads(content)
        df = json_normalize(contentInJson)
        df = df[['id', 'AuditID', 'RevisionNumber', 'FacilityName', 'FacilityID', 'Auditor1', 'Auditor2', 'Auditor3',
                 'AuditDate', 'RepDate', 'LinacModel', 'LinacManufacturer', 'PlanningSystemManufacturer', 'tps',
                 'Algorithm', 'kqFac', 'ACDS', 'Phantom']]

        fac_df = json_normalize(contentInJson, record_path='facilityOutput', record_prefix='fac')
        fac_df.columns = fac_df.columns.str.replace('energy', "")

        tpr_df = json_normalize(contentInJson, record_path='TPR', record_prefix='tpr')
        tpr_df.columns = tpr_df.columns.str.replace('energy', "")

        reading_df = json_normalize(contentInJson, record_path='Reading')
        reading_df = reading_df[
            ['Reading_101106', 'Reading_110106', 'Reading_205106', 'Reading_208106', 'Reading_205206',
             'Reading_208206', 'Reading_205306', 'Reading_208306', 'Reading_303106', 'Reading_305106',
             'Reading_403106', 'Reading_405106', 'Reading_103110', 'Reading_110110', 'Reading_303110',
             'Reading_305110', 'Reading_403110', 'Reading_405110', 'Reading_103115', 'Reading_110115',
             'Reading_303115', 'Reading_305115', 'Reading_403115', 'Reading_405115', 'Reading_103118',
             'Reading_110118', 'Reading_303118', 'Reading_305118', 'Reading_403118', 'Reading_405118',
             'Reading_101105', 'Reading_110105', 'Reading_303105', 'Reading_305105', 'Reading_103109',
             'Reading_110109', 'Reading_303109', 'Reading_305109']]
        misdelivery_df = json_normalize(contentInJson, record_path='Misdelivery')

        imrt_df = json_normalize(contentInJson, record_path='IMRT')
        imrt_misdelivery_df = json_normalize(contentInJson, record_path='IMRT_misdelivery',
                                             record_prefix='imrt_misdelivery_')

        table = pd.concat([df, fac_df, tpr_df, reading_df, misdelivery_df, imrt_df, imrt_misdelivery_df], axis=1)
        table.to_excel("download/" + "list" + ".xlsx", index=False)
        print("listResults")
        print(data.decode("utf-8"))
        return res

    def updateResultsWithIDs(self, resultIds):
        resultsList = self.parseExcel()
        if len(resultIds) != len(resultsList):
            print("The number of results ids does not match with the number of results in excel")
            return
        for i in range(len(resultIds)):
            payload = resultsList[i]
            headers = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
            }
            self.conn.request("PUT", "/graphs/results/" + resultIds[i] + "/", payload, headers)
            res = self.conn.getresponse()
            data = res.read()
            print("updateResultsWithIDs")
            print(data.decode("utf-8"))

    def updateResults(self):
        resultsList, ids = self.parseExcel()
        for i in range(len(ids)):
            payload = resultsList[i]
            headers = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
            }
            self.conn.request("PUT", "/graphs/results/" + ids[i] + "/", payload, headers)
            res = self.conn.getresponse()
            # print("listResults: res.status, res.reason")
            # print(res.status, res.reason)
            data = res.read()
            print("updateResults")
            print(data.decode("utf-8"))
            print(ids[i])
            return res

    def retrieveResultWithID(self, resultID):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("GET", "/graphs/results/" + resultID + "/", payload, headers)
        res = self.conn.getresponse()
        print("retrieveResultWithID: res.status, res.reason")
        print(res.status, res.reason)
        data = res.read()
        content = bytes.decode(data, 'utf-8')
        df = json_normalize(json.loads(content))
        df.to_excel("download/" + "retrive" + resultID + datetime.now().strftime("%Y%m%d%H%H%S") + ".xlsx")
        print("retrieveResultWithID")
        print(data.decode("utf-8"))
        return res

    def deleteResultWithID(self, resultID):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("DELETE", "/graphs/results/" + resultID + "/", payload, headers)
        res = self.conn.getresponse()
        # print("deleteResultWithID: res.status, res.reason")
        # print(res.status, res.reason)
        data = res.read()
        print(data.decode("utf-8"))
        return res

    # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Get resultRequest HTTP method                                                      #
    # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def get_insertNewResult_HTTPRequest(self):
        request = self.insertNewResult()
        if request.status == 201:
            return request.status
        else:
            print("The insertNewResult request has not succeeded ")
            return None

    def get_listResults_HTTPRequest(self):
        request = self.listResults()
        if request.status == 200:
            # print("The HTTP 200 OK success status response code")
            # print("request")
            # print(request.status, request.reason)
            return request.status
        else:
            print("The listResults request has not succeeded ")
            return None

    def get_updateResults_HTTPRequest(self):
        request = self.updateResults()
        if request.status == 200:
            return request.status
        else:
            print("The updateResults request has not succeeded ")
            return None

    def get_retrieveResultWithID_HTTPRequest(self, resultID):
        request = self.retrieveResultWithID(resultID)
        print("request")
        print(request.status)
        if request.status == 200:
            print("The retrieveResultWithID HTTP 200 OK success status response code")
            return request.status
        else:
            print("The retrieveResultWithID request has not succeeded ")
            return None

    def get_deleteResultWithID_HTTPRequest(self, resultID):
        request = self.deleteResultWithID(resultID)
        print("request")
        print(request.status)
        if request.status == 204:
            return request.status
        if request.status == 404:
            return request.status
        else:
            print("The deleteResultWithID Request has not succeeded ")
            return None

obj = resultRequest()
# obj.insertNewResult()
# obj.listResults()
# obj.updateResultsWithIDs('84')
# obj.updateResults()
# obj.retrieveResultWithID('61')



