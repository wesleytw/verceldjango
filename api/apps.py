import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    model = joblib.load(MODEL_FILE)
    svm_MODEL_FILE = os.path.join(settings.MODELS, "SVM.joblib")
    svm_model = joblib.load(svm_MODEL_FILE)


    