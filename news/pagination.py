from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response


# TODO Increase page size to 100 and max to 100

#
# {
#     "by": "cecil",
#     "id": 364341333289998,
#     "time": "2023-06-23T10:21:40.660847Z",
#     "title": "The wonders",
#     "score": 77,
#     "type": "job",
#     "url": "https://www.django-rest-framework.org/api-guide/pagination/"
# }
#

