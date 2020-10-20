import unittest
from unittest.mock import patch
from LocalProgram.resultRequest import resultRequest
from LocalProgram.graphRequest import graphRequest

class UnitTest(unittest.TestCase):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Unittest for resultRequest class                                                   #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def test_insertNewResultRequest(self):
        try:
            obj = resultRequest()
            response = obj.get_insertNewResult_HTTPRequest()
            self.assertEqual(response, 201)
            print("The insertNewResult HTTP 201 Created success status response code")
        except AssertionError:
            print("The insertNewResult request has not succeeded ")

    def test_listResultsRequest(self):
        try:
            obj = resultRequest()
            response = obj.get_listResults_HTTPRequest()
            self.assertEqual(response, 200)
            print("The listResults HTTP 200 OK success status response code")
        except AssertionError:
            print("The listResults request has not succeeded ")

    def test_updateResultsRequest(self):
        try:
            obj = resultRequest()
            response = obj.get_updateResults_HTTPRequest()
            self.assertEqual(response, 200)
            print("The updateResults HTTP 200 OK success status response code")
        except AssertionError:
            print("The updateResults request has not succeeded ")

    def test_retrieveResultWithID_Request(self):
        try:
            obj = resultRequest()
            response = obj.get_retrieveResultWithID_HTTPRequest('2')
            self.assertEqual(response, 200)
            print("The retrieveResultWithID HTTP 200 OK success status response code")
        except AssertionError:
            print("The retrieveResultWithID request has not succeeded ")

    def test_deleteResultWithID_Request(self):
        try:
            obj = resultRequest()
            response = obj.get_deleteResultWithID_HTTPRequest('2')
            if response == 204:
                self.assertEqual(response, 204)
                print("The deleteResultWithID HTTP 204 No Content success status response code")

            if response == 404:
                self.assertEqual(response, 404)
                print("The deleteResultWithID HTTP 404 Not Found success status response code")

        except AssertionError:
            print("The deleteResultWithID request has not succeeded ")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Unittest for graphRequest class                                                    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def test_list_graphs_Request(self):
        try:
            obj = graphRequest()
            response = obj.get_list_graphs_HTTPRequest()
            self.assertEqual(response, 200)
            print("The list_graphs HTTP 200 OK success status response code")
        except AssertionError:
            print("The list_graphs request has not succeeded ")

    def test_get_delete_graph_Request(self):
        try:
            obj = graphRequest()
            response = obj.get_delete_graph_HTTPRequest('2')
            self.assertEqual(response, 200)
            print("The delete_graph HTTP 200 OK success status response code")
        except AssertionError:
            print("The delete_graph request has not succeeded ")

    def test_plot_graph_NDS_3DCRT_Request(self):
        try:
            obj = graphRequest()
            response = obj.get_plot_graph_NDS_3DCRT_HTTPRequest("all", '{"Drever": [308], "Avocet": [106, 302]}')
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_3DCRT HTTP 200 OK success status response code")
        except AssertionError:
            print("The plot_graph_NDS_3DCRT request has not succeeded ")


    def test_get_plot_graph_NDS_IMR_Request(self):
        try:
            obj = graphRequest()
            response = obj.get_plot_graph_NDS_IMRT_HTTPRequest("std", '{"Drever": [308], "Avocet": [106, 302]}')
            self.assertEqual(response, 200)
            print("The plot_graph_NDS_IMR HTTP 200 OK success status response code")
        except AssertionError:
            print("The plot_graph_NDS_IMR request has not succeeded ")
