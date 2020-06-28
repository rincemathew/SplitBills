from django.urls import path, include

from entries import views
from rest_framework import routers
from .views import PlanViewSet

router = routers.DefaultRouter()
router.register('plans', PlanViewSet)

urlpatterns = [
    path('hello/', include(router.urls)),
]