from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class QuestionModelformVSPagination(PageNumberPagination):
    page_size = 1
    def get_paginated_response(self, data):
        return Response({
            "links":  {
                "next":     self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "count":      self.page.paginator.count,
            "results":    data,
            "pageCount":  self.page.paginator.num_pages,
            "pageNumber": self.page.number,
            "pageSize":   self.page.paginator.per_page

        })