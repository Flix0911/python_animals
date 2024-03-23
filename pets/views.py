from .models import Turtle
from rest_framework import viewsets, permissions
from .serializer import TurteSerializer

class TurtleViewSet(viewsets.ModelViewSet):
    # That order_by('id') is optional ~ it's a method ordering
    queryset=Turtle.objects.all().order_by('id')
    
    serializer_class=TurteSerializer
    
    permission_classes=[permissions.AllowAny]