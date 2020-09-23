import pandas as pd
import json
import http.client
import mimetypes
from pandas import json_normalize
from LocalProgram.config import *
from datetime import datetime


class resultRequest:

    def __init__(self):
        self.authorization = authorization
        self.host = host
        self.port = port
        self.conn = http.client.HTTPConnection(self.host,self.port)

    def parseExcel(self) -> [str]:
        filename = "upload/uploadingData.xlsx"
        df = pd.read_excel(filename) # read uploadingData.xlsx
        df["AuditDate"] = df["AuditDate"].dt.strftime("%Y-%m-%d") # covert 10/5/2016 to 2016-10-05
        resultList = []

        for i in range(len(df)):
            unested = df.loc[i,"AuditID":"Phantom"].to_json()
            # get excel content from "AuditID" to "Phantom"as JSON

            facilityOutput = df.loc[i,"fac_6":"fac_10FFF"].to_json().replace("fac","energy")
            # replace 'fac' as 'energy' from "fac_6" to "fac_10FFF"

            tpr = df.loc[i,"TPR_6":"TPR_10FFF"].to_json().replace("TPR","energy")
            # replace 'fac' as 'energy' from "TPR_6" to "TPR_10FFF"

            readings = df.loc[i,"Reading_101106":"Reading_305109"].to_json()
            # get excel content from "AuditID" to "Phantom"as JSON

            misdelivery = df.loc[i,"Misdelivery_101106":"Misdelivery_305109"].to_json()
            # get excel content from "Misdelivery_101106" to "Misdelivery_305109"as JSON

            result = json.loads(unested)
            result.update({"facilityOutput":[json.loads(facilityOutput)]}) # update facilityOutput dataset
            result.update({"TPR":[json.loads(tpr)]}) # update TPR dataset
            result.update({"Reading":[json.loads(readings)]}) # update Reading dataset
            result.update({"Misdelivery":[json.loads(misdelivery)]}) # update Misdelivery dataset
            resultList.append(json.dumps(result))
            #append facilityOutput dataset,TPR dataset,Reading dataset,Misdelivery dataset into resultList
        return resultList


    def insertNewResult(self):
        resultsList = self.parseExcel()
        for result in resultsList:
            payload = result
            headers = {
                'Authorization': self.authorization,
                'Content-Type': 'application/json'
            }
            self.conn.request("POST", "/graphs/results/", payload, headers)
            res = self.conn.getresponse()
            data = res.read()
            print('hi'+data.decode("utf-8"))

    def listResults(self):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("GET", "/graphs/results/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        content = bytes.decode(data, 'utf-8')
        df = json_normalize(json.loads(content))
        df.to_excel("download/" + "list" + datetime.now().strftime("%Y%m%d%H%H%S") + ".xlsx")
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


resultRequest().parseExcel()
resultRequest().insertNewResult()
# resultRequest().listResults()
# resultRequest().updateResultsWithIDs()
# resultRequest().retrieveResultWithID()
# resultRequest().deleteResultWithID()
