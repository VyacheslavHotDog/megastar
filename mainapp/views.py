from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response

from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet
    """

    def retrieve(self, request, pk=None):

        # Также можно использовать Worker.objects.prefetch_related('books).get(pk=pk) но всегда будет выполняться два запроса
        cursor = connection.cursor()
        cursor.execute("""select mainapp_writer.*, 
            (
            SELECT json_agg(row_to_json(x))
            FROM (
            SELECT mainapp_book.id, mainapp_book.name FROM mainapp_book
            Where mainapp_book.writer_id = mainapp_writer.id
            ) x
            )books
            FROM mainapp_writer
            Where mainapp_writer.id = %s;""", [pk])


        res = dictfetchall(cursor)
        if not res:
            raise Http404()
        return Response(res[0])


