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
        # read excel
        filename = "upload/AllData_copy.xlsx"
        df = pd.read_excel(filename)
        df["AuditDate"] = pd.to_datetime(df["AuditDate"], errors='coerce')
        df["AuditDate"] = df["AuditDate"].dt.strftime("%Y-%m-%d")

        # round following columns to 4 digits
        roundIndex = ['code_101106', 'code_110106', 'code_205106', 'code_208106', 'code_205206',
                      'code_208206', 'code_205306', 'code_208306', 'code_303106', 'code_305106',
                      'code_403106', 'code_405106', 'code_103110', 'code_110110', 'code_303110',
                      'code_305110', 'code_403110', 'code_405110', 'code_103115', 'code_110115',
                      'code_303115', 'code_305115', 'code_403115', 'code_405115', 'code_103118',
                      'code_110118', 'code_303118', 'code_305118', 'code_403118', 'code_405118',
                      'code_101105', 'code_110105', 'code_303105', 'code_305105', 'code_103109',
                      'code_110109', 'code_303109', 'code_305109', 'code_c6_p11_6', 'code_c6_p12_6', 'code_c6_p13_6',
                      'code_c6_p14_6', 'code_c6_p15_6', 'code_c6_p16_6', 'code_c6_p17_6', 'code_c7_p11_6',
                      'code_c7_p12_6', 'code_c7_p13_6', 'code_c7_p14_6',
                      'code_c7_p15_6', 'code_c7_p16_6', 'code_c7_p17_6', 'code_c8_p11_6', 'code_c8_p12_6',
                      'code_c8_p13_6', 'code_c8_p14_6', 'code_c8_p15_6',
                      'code_c8_p17_6', 'code_c8_p18_6', 'code_c6_p11_10', 'code_c6_p12_10', 'code_c6_p13_10',
                      'code_c6_p14_10', 'code_c6_p15_10',
                      'code_c6_p16_10', 'code_c6_p17_10', 'code_c7_p11_10', 'code_c7_p12_10', 'code_c7_p13_10',
                      'code_c7_p14_10', 'code_c7_p15_10',
                      'code_c7_p16_10', 'code_c7_p17_10', 'code_c8_p11_10', 'code_c8_p12_10', 'code_c8_p13_10',
                      'code_c8_p14_10', 'code_c8_p15_10',
                      'code_c8_p17_10', 'code_c8_p18_10', 'fac_6', 'fac_10', 'fac_15', 'fac_18', 'fac_6FFF',
                      'fac_10FFF', 'TPR_6',
                      'TPR_10', 'TPR_15', 'TPR_18', 'TPR_6FFF', 'TPR_10FFF', ]
        decimals = pd.Series([4 for _ in range(92)], index=roundIndex)
        df = df.round(decimals)

        ids = []
        resultList = []
        for i in range(len(df)):
            id = df.loc[i, 'id']
            if not math.isnan(id):
                ids.append(str(int(id)))
            unested = df.loc[i, "AuditID":"Phantom"].to_json()
            facilityOutput = df.loc[i, "fac_6":"fac_10FFF"].to_json().replace("fac", "energy")
            tpr = df.loc[i, "TPR_6":"TPR_10FFF"].to_json().replace("TPR", "energy")
            readings = df.loc[i, "code_101106":"code_305109"].to_json()
            misdelivery = df.loc[i, "Misdelivery_101106":"Misdelivery_305109"].to_json().replace("Misdelivery_", "code_")
            imrt = df.loc[i, "code_c6_p11_6":"code_c8_p18_10"].to_json()
            imrt_misdelivery = df.loc[i, "imrt_misdelivery_c6_p11_6":"imrt_misdelivery_c8_p18_10"].to_json().replace(
                "imrt_misdelivery_", "code_")

            result = json.loads(unested)
            result.update({"facilityOutput": [json.loads(facilityOutput)]})
            result.update({"TPR": [json.loads(tpr)]})
            result.update({"Nds_3dcrt": [json.loads(readings)]})
            result.update({"Nds_3dcrt_misdelivery": [json.loads(misdelivery)]})
            result.update({"Nds_imrt": [json.loads(imrt)]})
            result.update({"Nds_imrt_misdelivery": [json.loads(imrt_misdelivery)]})
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
        print(data.decode("utf-8"))
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

        reading_df = json_normalize(contentInJson, record_path='Nds_3dcrt')
        reading_df = reading_df[
            ['code_101106', 'code_110106', 'code_205106', 'code_208106', 'code_205206',
             'code_208206', 'code_205306', 'code_208306', 'code_303106', 'code_305106',
             'code_403106', 'code_405106', 'code_103110', 'code_110110', 'code_303110',
             'code_305110', 'code_403110', 'code_405110', 'code_103115', 'code_110115',
             'code_303115', 'code_305115', 'code_403115', 'code_405115', 'code_103118',
             'code_110118', 'code_303118', 'code_305118', 'code_403118', 'code_405118',
             'code_101105', 'code_110105', 'code_303105', 'code_305105', 'code_103109',
             'code_110109', 'code_303109', 'code_305109']]
        misdelivery_df = json_normalize(contentInJson, record_path='Nds_3dcrt_misdelivery')

        imrt_df = json_normalize(contentInJson, record_path='Nds_imrt')
        imrt_misdelivery_df = json_normalize(contentInJson, record_path='Nds_imrt_misdelivery',
                                             record_prefix='imrt_misdelivery_')

        table = pd.concat([df, fac_df, tpr_df, reading_df, misdelivery_df, imrt_df, imrt_misdelivery_df], axis=1)
        table.to_excel("download/" + "list" + ".xlsx", index=False)
        print("listResults")
        print(data.decode("utf-8"))
        return res

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
