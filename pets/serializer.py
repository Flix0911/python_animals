from .models import Turtle
from rest_framework import serializers

class TurteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Turtle
        fields=('id', 'name', 'age')