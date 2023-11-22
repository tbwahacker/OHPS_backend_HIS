from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
class RegistrationViewSet (viewsets.ModelViewSet):
    queryset = models.Registration.objects.all()
    serializer_class = serializer.RegistrationSerializer

    #list(),retrieve(),create(),update(),destroy()