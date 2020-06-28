from rest_framework import serializers
from .models import Plans


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ['name_plan', 'status_plan'
                  ]
