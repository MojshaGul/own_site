from django.contrib import admin
from django.urls import path
from mai.views import *

urlpatterns = [
    path('', baseView.as_view(), name='cbv_page'),
    path('test_page/', baseView.as_view(), name='cbv_page2'),
    path("guide_page/", aboutView(), name='guide'),
    path('test_page/', baseView.as_view(), name='cbv_page2'),
    path("anketa/", anketaView(), name='anketa'),
]
