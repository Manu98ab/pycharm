from django.urls import path

from . import views

urlpatterns = [
    path('Wish/<str:name>',views.wish,name="wish")
]