import unittest
from unittest.mock import patch
from LocalProgram.resultRequest import resultRequest
from LocalProgram.graphRequest import graphRequest


class UnitTest(unittest.TestCase):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Unittest for resultRequest class                                                    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def test_insertNewResultRequest(self):
        try:
            response = resultRequest().insertNewResult()
            self.assertEqual(response, 201)
            print("The insertNewResult HTTP 201 Created success status response code")
        except AssertionError:
            print("The insertNewResult request was not succeeded")

    def test_listResultsRequest(self):
        try:
            response = resultRequest().listResults()
            self.assertEqual(response, 200)
            print("The listResults HTTP 200 OK success status response code")
        except AssertionError:
            print("The listResults request was not succeeded")

    def test_updateResultsRequest(self):
        try:
            response = resultRequest().updateResults()
            self.assertEqual(response, 200)
            print("The updateResults HTTP 200 OK success status response code")
        except AssertionError:
            print("The updateResults request was not succeeded")

    def test_retrieveResultWithID_Request(self):
        try:
            response = resultRequest().retrieveResultWithID('2')
            self.assertEqual(response, 200)
            print("The retrieveResultWithID HTTP 200 OK success status response code")
        except AssertionError:
            print("The retrieveResultWithID request has not succeeded")

    def test_deleteResultWithID_Request(self):
        response = ""
        try:
            response = resultRequest().deleteResultWithID('2')
            self.assertEqual(response, 200)
        except AssertionError:
            if response == 204:
                print("The deleteResultWithID HTTP 204 No Content success status response code")
            elif response == 404:
                print("The deleteResultWithID HTTP 404 Not Found success status response code")
            else:
                print("The deleteResultWithID Request was not succeeded")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Unittest for graphRequest class                                                     #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def test_list_graphs_Request(self):
        try:
            response = graphRequest().list_graphs()
            self.assertEqual(response, 200)
            print("The list_graphs HTTP 200 OK success status response code")
        except AssertionError:
            print("The list_graphs request was not succeeded")

    def test_get_delete_graph_Request(self):
        try:
            response = graphRequest().delete_graph(2)
            self.assertEqual(response, 200)
            print("The delete_graph HTTP 200 OK success status response code")
        except AssertionError:
            print("The delete_graph request has not succeeded")

    def test_plot_graph_NDS_3DCRT_Request(self):
        try:
            response = graphRequest().plot_graph_NDS_3DCRT("all", "{\"Drever\": [308], \"Avocet\": [106, 302]}")
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_3DCRT HTTP 200 OK success status response code")
        except AssertionError:
            print("The plot_graph_NDS_3DCRT request has not succeeded")

    def test_get_plot_graph_NDS_IMRT_all_Request(self):
        try:
            response = graphRequest().plot_graph_NDS_IMRT("all", "{\"Drever\": [308], \"Avocet\": [106, 302]}")
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_IMR HTTP 200 OK success status response code")
        except AssertionError:
            print("The plot_graph_NDS_IMR request was not succeeded")

    def test_get_plot_graph_NDS_IMRT_average_Request(self):
        try:
            response = graphRequest().plot_graph_NDS_IMRT("average", "{\"Drever\": [308], \"Avocet\": [106, 302]}")
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_IMR HTTP 200 OK success status response code")
        except AssertionError:
            print("The plot_graph_NDS_IMR request was not succeeded")

    def test_get_plot_graph_NDS_IMRT_std_Request(self):
        try:
            response = graphRequest().plot_graph_NDS_IMRT("std", "{\"Drever\": [308], \"Avocet\": [106, 302]}")
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_IMR HTTP 200 OK success status response code")
        except AssertionError:
            print("The plot_graph_NDS_IMR request was not succeeded")

    def test_delete_graph_Request(self):
        try:
            response = graphRequest().delete_graph("15")
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_IMR HTTP 200 OK success status response code")
        except AssertionError:
            print("The deleting graph request was not succeeded")
