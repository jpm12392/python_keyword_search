from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/search/', SearchKeywordAPIView.as_view(), name='search'),
]