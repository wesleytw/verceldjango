import os
import joblib
from django.apps import AppConfig
from django.conf import settings
# from .dev import DecisionTreeModel


class ApiConfig(AppConfig):
    name = 'api'
    # MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    # model = joblib.load(MODEL_FILE)
    model = joblib.load(".dev.DecisionTreeModel.joblib")
