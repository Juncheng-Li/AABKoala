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

    # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Get graphRequest HTTP method                                                                 #
    # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def get_list_graphs_HTTPRequest(self):
        request = self.list_graphs()
        if request.status == 200:
            return request.status
        else:
            print("The list_graphs request has not succeeded ")
            return None

    def get_plot_graph_NDS_3DCRT_HTTPRequest(self, mode, facilities):
        request = self.plot_graph_NDS_3DCRT(mode, facilities)
        if request.status == 200:
            # print("get_plot_graph_NDS_3DCRT_HTTPRequest request")
            # print(request.status)
            return request.status
        else:
            # print("The list_graphs request has not succeeded ")
            return None

    def get_plot_graph_NDS_IMRT_HTTPRequest(self, mode, facilities):
        request = self.plot_graph_NDS_IMRT(mode, facilities)
        if request.status == 200:
            print("get_plot_graph_NDS_3DCRT_HTTPRequest request")
            print(request.status)
            return request.status
        else:
            # print("The list_graphs request has not succeeded ")
            return None

    def get_delete_graph_HTTPRequest(self, resultID):
        request = self.delete_graph(resultID)
        if request.status == 200:
            return request.status
        else:
            return None

# graphRequest().list_graphs()
# graphRequest().delete_graph("15")
# graphRequest().retrieve_graph("3DCRT_1600914975424.png")

# graphRequest().plot_graph_NDS_3DCRT("all", '{"Drever": [308], "Avocet": [106, 302]}')
# graphRequest().plot_graph_NDS_IMRT("std", '{"Drever": [308], "Avocet": [106, 302]}')
