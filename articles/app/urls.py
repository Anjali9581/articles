from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('one/<int:pk>',views.display,name='display'),
    path('1',views.about,name="aboutdetails"),
]