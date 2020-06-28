from django.urls import path

from entries import views
from .views import Test

urlpatterns = [
    path('demo/', views.first),
    path('new/', Test.as_view()),
]