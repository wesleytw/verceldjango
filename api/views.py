from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item
from .serializers import ItemSerializer
from verceldjango.call import call

# from ml_models.dev.decisiontree import call
import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response


class Prediction(APIView):
    def get(self, request):  # get, post...
        #data = request.data
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = ApiConfig.model
        # predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)
    def post(self, request):  # get, post...
        #data = request.data
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = ApiConfig.model
        # predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)


@api_view(['GET'])
def getData(req):
    person = {'name': 'wes', 'age': 20}
    return Response(person)


@api_view(['POST'])
def resItem(req):
    # serializer = ItemSerializer(data=req.data)
    # if serializer.is_valid():
    #   serializer.save()
    #   return Response(serializer.data)
    return Response(req.data)


@api_view(['POST'])
def saveItem(req):
    serializer = ItemSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def callItem(req):
    item = call(req.data)
    print(req, item)
    return Response(item)


@api_view(['GET'])
def ml(req):
    person = {'name': 'wes', 'age': 20}
    return Response(person)
