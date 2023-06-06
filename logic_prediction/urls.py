from django.urls import path
from . import views
app_name = "logic_prediction"
urlpatterns  = [
    path("prediction_view/", views.prediction_view, name = "prediction_view"),
    ]