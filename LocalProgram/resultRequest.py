import pandas as pd
import json
import http.client
import mimetypes
from LocalProgram.config import *

class resultRequest:

    def __init__(self):
        self.authorization = authorization
        self.host = host
        self.port = port
        self.conn = http.client.HTTPConnection(self.host,self.port)

    def parseExcel(self) -> [str]:
        filename = "upload/uploadingData.xlsx"
        df = pd.read_excel(filename)
        resultList = []

        for i in range(len(df)):
            unested = df.loc[i,"AuditID":"Phantom"].to_json()
            facilityOutput = df.loc[i,"fac_6":"fac_10FFF"].to_json().replace("fac","energy")
            trp = df.loc[i,"TRP_6":"TRP_10FFF"].to_json().replace("TRP","energy")
            readings = df.loc[i,"Reading_101106":"Reading_305109"].to_json()
            misdelivery = df.loc[i,"Misdelivery_101106":"Misdelivery_305109"].to_json()

            result = json.loads(unested)
            result.update({"facilityOutput":[json.loads(facilityOutput)]})
            result.update({"TRP":[json.loads(trp)]})
            result.update({"Reading":[json.loads(readings)]})
            result.update({"Misdelivery":[json.loads(misdelivery)]})

            resultList.append(json.dumps(result))

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
            print(data.decode("utf-8"))

    def listResults(self):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("GET", "/graphs/results/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        """write some code here to decode the json to excel"""

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

    def retriveResultWithID(self, resultID):
        payload = ''
        headers = {
            'Authorization': self.authorization,
        }
        self.conn.request("GET", "/graphs/results/" + resultID + "/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
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


