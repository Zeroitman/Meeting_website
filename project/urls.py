from django.urls import path
from project.views import *

urlpatterns = [
    path('clients/create', RegisterUserView.as_view())
]
