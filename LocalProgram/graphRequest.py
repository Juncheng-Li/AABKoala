import http.client
import urllib.request
import os
import json


class graphRequest:

    def __init__(self):
        self.authorization = "Basic cm9vdDpyb290"
        self.host = "127.0.0.1"
        self.port = 8000
        self.conn = http.client.HTTPConnection(self.host, self.port)

    def list_graphs(self):
        payload = {}
        headers = {}
        self.conn.request("GET", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def retrieve_graph(self, fileName):
        localPath = os.path.split(os.path.realpath(__file__))[0]+"/download/"+fileName
        filePath = "http://"+self.host+":"+str(self.port)+"/graph/"+fileName
        urllib.request.urlretrieve(filePath, localPath)

    def plot_graph_NDS_3DCRT(self, mode, facilities):
        payload = "{   \n    \"graphType\": \"NDS_3DCRT\",\n    \"mode\": \"%s\",\n    \"facilitys\":%s\n}" % (mode, facilities)
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        self.conn.request("POST", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        graphInfo = json.loads(data.decode("utf-8"))
        self.retrieve_graph(graphInfo["fileName"])

    def plot_graph_NDS_IMRT(self, mode, facilities):
        payload = "{   \n    \"graphType\": \"NDS_IMRT\",\n    \"mode\": \"%s\",\n    \"facilitys\":%s\n}" % (mode, facilities)
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        self.conn.request("POST", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        graphInfo = json.loads(data.decode("utf-8"))
        self.retrieve_graph(graphInfo["fileName"])

    def delete_graph(self, graphID):
        payload = "{\n    \"graphs_list\":[%s]\n}" % graphID
        headers = {}
        self.conn.request("DELETE", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))


#graphRequest().list_graphs()
#graphRequest().delete_graph("151")
#graphRequest().retrieve_graph("3DCRT_1600914975424.png")
#graphRequest().plot_graph_NDS_3DCRT("all", '{"Drever": [91], "Avocet": [99, 101]}')
graphRequest().plot_graph_NDS_IMRT("std", '{"Drever": [91], "Avocet": [99, 101]}')

