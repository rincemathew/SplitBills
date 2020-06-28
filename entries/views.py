from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Plans
from rest_framework import viewsets
from .serializers import PlansSerializer


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlansSerializer
    queryset = Plans.objects.all()
