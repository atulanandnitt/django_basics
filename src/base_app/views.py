from django.shortcuts import render
from rest_framework import (status)
from rest_framework.response import Response
from base_app.services.v0_1.base import Base
from base_app.services.v0_1.feature_math.summation import Summation

# Create your views here.

class Summation(Base):
    def post(self, request):
        import ipdb; ipdb.set_trace()
        try:
            request_data = request.data
            sol = 0
            print(request_data, type(request_data))
            # a = request_data.get('a')
            # b = request_data.get('b')
            obj_s = Summation()
            sol = obj_s.addition(request_data)

            respose = {"sol": sol}
            return Response(respose,
            status = status.HTTP_200_OK,
            content_type='application/json')
        except Exception as ex:
            dummy_respose = dict()
            return Response(dummy_respose,
            status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content_type='application/json')