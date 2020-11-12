from django.urls import path
from . import views

urlpatterns = [
    path('',views.about),
    path('about/',views.home),
    path('contact/',views.contact),
    path('services/',views.services),
]