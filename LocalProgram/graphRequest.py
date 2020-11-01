import http.client
import urllib.request
import os
import json
from LocalProgram.config import *


class graphRequest:

    def __init__(self):
        self.authorization = authorization
        self.host = host
        self.port = port
        self.conn = http.client.HTTPConnection(self.host, self.port)

    def list_graphs(self):
        payload = {}
        headers = {}
        self.conn.request("GET", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def retrieve_graph(self, fileName):
        localPath = os.path.split(os.path.realpath(__file__))[0] + "/download/" + fileName
        filePath = "http://" + self.host + ":" + str(self.port) + "/graph/" + fileName
        urllib.request.urlretrieve(filePath, localPath)

    def plot_graph_NDS_3DCRT(self, mode, facilities):
        payload = "{   \n    \"graphType\": \"NDS_3DCRT\",\n    \"mode\": \"%s\",\n    \"facilitys\":%s\n}" % (
            mode, facilities)
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        self.conn.request("POST", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        # print("plot_graph_NDS_3DCRT: res.status, res.reason")
        # print(res.status, res.reason)
        data = res.read()
        print(data.decode("utf-8"))
        graphInfo = json.loads(data.decode("utf-8"))
        self.retrieve_graph(graphInfo["fileName"])
        return res

    def plot_graph_NDS_IMRT(self, mode, facilities):
        payload = "{   \n    \"graphType\": \"NDS_IMRT\",\n    \"mode\": \"%s\",\n    \"facilitys\":%s\n}" % (
            mode, facilities)
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        self.conn.request("POST", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        # print("plot_graph_NDS_IMRT: res.status, res.reason")
        # print(res.status, res.reason)
        data = res.read()
        print(data.decode("utf-8"))
        graphInfo = json.loads(data.decode("utf-8"))
        self.retrieve_graph(graphInfo["fileName"])
        return res

    def delete_graph(self, graphID):
        payload = "{\n    \"graphs_list\":[%s]\n}" % graphID
        headers = {}
        self.conn.request("DELETE", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        return res

