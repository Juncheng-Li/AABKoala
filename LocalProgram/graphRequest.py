import http.client
import urllib.request
import os


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

    def plot_graph(self, resultIDs):
        payload = "{\n    \"results_list\":%s\n}"%resultIDs
        headers = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }
        self.conn.request("POST", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def delete_graph(self, graphID):
        payload = "{\n    \"graphs_list\":[%d]\n}"%graphID
        headers = {}
        self.conn.request("DELETE", "/graphs/graphManage/", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))


#graphRequest().list_graphs()
#graphRequest().delete_graph(16)
#graphRequest().plot_graph("[1,2,3]")
graphRequest().retrieve_graph("3DCRT_1600153340110.png")
