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
import json


class Prediction(APIView):
    # def get(self, request):  # get, post...
    #     #data = request.data
    #     age = request.GET.get('age')
    #     gender = request.GET.get('gender')
    #     bp = request.GET.get('bp')
    #     cholesterol = request.GET.get('cholesterol')
    #     salt = request.GET.get('salt')
    #     model = request.GET.get('model')
    #     if (model == "tree"):
    #         dtree = ApiConfig.model
    #     if (model == "svm"):
    #         dtree = ApiConfig.svm_model
    #     # predict using independent variables
    #     PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
    #     response_dict = {"Predicted drug": PredictionMade}
    #     print(response_dict)
    #     return Response(response_dict, status=200)
    def post(self, request):  # get, post...
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print("RRRRRrequest",request,"bo",body_data['age'])
        #data = request.data
        if (request.GET.get('age')):
            age = request.GET.get('age')
            gender = request.GET.get('gender')
            bp = request.GET.get('bp')
            cholesterol = request.GET.get('cholesterol')
            salt = request.GET.get('salt')
            model = request.GET.get('model')
        else:
            age = body_data['age']
            gender = body_data['gender']
            bp = body_data['bp']
            cholesterol = body_data['cholesterol']
            salt = body_data['salt']
            model = body_data['model']
        if (model == "tree"):
            dtree = ApiConfig.model
        elif (model == "svm"):
            dtree = ApiConfig.svm_model
        else:
            dtree = ApiConfig.model
        # predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Model":model,"salt": salt, "Predicted drug": PredictionMade}
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
