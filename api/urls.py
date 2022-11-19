from django.urls import path
from .views import getData, resItem, saveItem, callItem, ml, Prediction

urlpatterns = [
    # path('', getData),
    path('/res', resItem),
    path('/save', saveItem),
    path('/call', callItem),
    path('/ml', ml),
    path('', Prediction.as_view(), name='predict'),
]
