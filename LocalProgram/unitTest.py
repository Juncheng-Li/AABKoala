import unittest
from unittest.mock import patch
from LocalProgram.resultRequest import resultRequest
from LocalProgram.graphRequest import graphRequest



class UnitTest(unittest.TestCase):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Unittest for result request class                                                   #
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
    # Unittest for graph request class                                                    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def test_list_graphs_Request(self):
        try:
            obj = graphRequest()
            response = obj.get_list_graphs_HTTPRequest()
            self.assertEqual(response, 200)
            print("The list_graphs HTTP 200 OK success status response code")
        except AssertionError:
            print("The list_graphs request has not succeeded ")
