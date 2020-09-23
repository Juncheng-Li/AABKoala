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
        self.conn = http.client.HTTPConnection(self.host,self.port)

    def parseExcel(self):
        filename = "upload/uploadingData.xlsx"
        df = pd.read_excel(filename)
        df["AuditDate"] = pd.to_datetime(df["AuditDate"], errors='coerce')
        df["AuditDate"] = df["AuditDate"].dt.strftime("%Y-%m-%d")
        resultList = []
        ids = []

        for i in range(len(df)):
            id = df.loc[i,'id']
            if not math.isnan(id):
                ids.append(str(int(id)))
            unested = df.loc[i,"AuditID":"Phantom"].to_json()
            facilityOutput = df.loc[i,"fac_6":"fac_10FFF"].to_json().replace("fac","energy")
            tpr = df.loc[i,"TPR_6":"TPR_10FFF"].to_json().replace("TPR","energy")
            readings = df.loc[i,"Reading_101106":"Reading_305109"].to_json()
            misdelivery = df.loc[i,"Misdelivery_101106":"Misdelivery_305109"].to_json()

            result = json.loads(unested)
            result.update({"facilityOutput":[json.loads(facilityOutput)]})
            result.update({"TPR":[json.loads(tpr)]})
            result.update({"Reading":[json.loads(readings)]})
            result.update({"Misdelivery":[json.loads(misdelivery)]})

            resultList.append(json.dumps(result))

        return (resultList, ids)

    def insertNewResult(self):
        resultsList = self.parseExcel()[0]
        for result in resultsList:
            payload = result
            headers = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
            }
            time1 = time.time()
            self.conn.request("POST", "/graphs/results/", payload, headers)
            res = self.conn.getresponse()
            time2 = time.time()
            data = res.read()
            print("insert request completed, takes time %d" %(time2-time1) + data.decode("utf-8"))

    def listResults(self):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        print("downloading the whole dataset...")
        self.conn.request("GET", "/graphs/results/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        content = bytes.decode(data, 'utf-8')
        contentInJson = json.loads(content)
        df = json_normalize(contentInJson)
        df = df[['id', 'AuditID', 'RevisionNumber', 'FacilityName', 'FacilityID', 'Auditor1', 'Auditor2', 'Auditor3',
                 'AuditDate', 'RepDate', 'LinacModel', 'LinacManufacturer', 'PlanningSystemManufacturer', 'tps',
                 'Algorithm', 'kqFac', 'ACDS', 'Phantom']]


        fac_df = json_normalize(contentInJson, record_path='facilityOutput', record_prefix='fac')
        fac_df.columns = fac_df.columns.str.replace('energy',"")

        tpr_df = json_normalize(contentInJson, record_path='TPR', record_prefix='tpr')
        tpr_df.columns = tpr_df.columns.str.replace('energy', "")

        reading_df = json_normalize(contentInJson, record_path='Reading')
        reading_df = reading_df[['Reading_101106','Reading_110106', 'Reading_205106', 'Reading_208106',	'Reading_205206',
                                 'Reading_208206', 'Reading_205306', 'Reading_208306', 'Reading_303106', 'Reading_305106',
                                 'Reading_403106', 'Reading_405106', 'Reading_103110', 'Reading_110110', 'Reading_303110',
                                 'Reading_305110', 'Reading_403110', 'Reading_405110', 'Reading_103115', 'Reading_110115',
                                 'Reading_303115', 'Reading_305115', 'Reading_403115', 'Reading_405115', 'Reading_103118',
                                 'Reading_110118', 'Reading_303118', 'Reading_305118', 'Reading_403118', 'Reading_405118',
                                 'Reading_101105', 'Reading_110105', 'Reading_303105', 'Reading_305105', 'Reading_103109',
                                 'Reading_110109', 'Reading_303109', 'Reading_305109']]
        misdelivery_df = json_normalize(contentInJson, record_path='Misdelivery')

        table = pd.concat([df, fac_df,tpr_df,reading_df, misdelivery_df], axis=1)
        table.to_excel("download/" + "list" + ".xlsx", index=False)
        print(data.decode("utf-8"))

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
            data = res.read()
            print(data.decode("utf-8"))
            print(ids[i])

    def retrieveResultWithID(self, resultID):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("GET", "/graphs/results/" + resultID + "/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        content = bytes.decode(data,'utf-8')
        df = json_normalize(json.loads(content))
        df.to_excel("download/" + "retrive" + resultID + datetime.now().strftime("%Y%m%d%H%H%S") + ".xlsx")
        print(data.decode("utf-8"))

    def deleteResultWithID(self, resultID):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("DELETE", "/graphs/results/" + resultID + "/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))