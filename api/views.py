from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item
from .serializers import ItemSerializer

@api_view (['GET'])
def getData(req):
  person = {'name': 'wes', 'age': 20}
  return Response(person)

@api_view (['POST'])
def resItem(req):
  # serializer = ItemSerializer(data=req.data)
  # if serializer.is_valid():
  #   serializer.save()
  #   return Response(serializer.data)
  return Response(req.data)

@api_view (['POST'])
def saveItem(req):
  serializer = ItemSerializer(data=req.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
