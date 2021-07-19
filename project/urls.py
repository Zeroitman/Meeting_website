from django.urls import path
from project.views import *

urlpatterns = [
    path('clients/create', RegisterUserView.as_view()),
    path('auth/login', MyObtainTokenPairView.as_view()),
    path('list', user_list),
    path('clients/<int:user_id>/match', grading)
]
