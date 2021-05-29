from .models import FindLane
from rest_framework import serializers


class FindLaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindLane
        fields = ['input_img','output_img']