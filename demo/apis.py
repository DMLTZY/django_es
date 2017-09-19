from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from . import utils


class TestESAPI(APIView):

    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        search = [x for x in request.POST.get('search').split(' ') if x]
        page_size = request.POST.get('page_size', '')
        if page_size:
            page_size = int(page_size)

        page = int(request.GET.get('page'))

        res = utils.search(search, page, page_size)

        return Response(data=res, status=status.HTTP_200_OK)
