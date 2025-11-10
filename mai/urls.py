from django.contrib import admin
from django.urls import path
from mai.views import *

urlpatterns = [
    path('', baseView.as_view(), name='cbv_page'),
    path("guide_page/", aboutView.as_view(), name='guide'),
    path("anketa/", anketaView.as_view(), name='anketa'),
    path("item/<int:id>", iteminfo.as_view(), name='item')
]
