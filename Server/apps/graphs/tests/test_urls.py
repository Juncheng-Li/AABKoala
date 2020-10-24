from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.graphs.views import GraphViewSet, ResultListViewSet


class TestUrls(SimpleTestCase):

    def test_urls_graph_manage(self):
        url = reverse('graph_manage')
        self.assertEqual(resolve(url).func.view_class, GraphViewSet)

    def test_urls_results_list(self):
        url = reverse('results_list')
        self.assertEqual(resolve(url).func.view_class, ResultListViewSet)
