from django.contrib.auth.models import User, Group
from nosotros.models import Nosotros, Profesional
from rest_framework import viewsets
from api.quickstart.serializers import UserSerializer, GroupSerializer, ProfesionalesSerializer , NosotrosSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
 
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfesionalesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalesSerializer

class NosotrosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Nosotros.objects.all()
    serializer_class = NosotrosSerializer