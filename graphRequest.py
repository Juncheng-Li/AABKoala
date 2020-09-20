import http.client

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

    def plot_graph(self, resultID):
        payload = "{\n    \"results_list\":[%d]\n}"%resultID
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

graphRequest().list_graphs()
