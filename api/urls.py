from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('/res', views.resItem),
    path('/save', views.saveItem),
    path('/call', views.callItem),
]