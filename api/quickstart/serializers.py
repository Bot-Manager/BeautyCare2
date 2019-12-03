from django.contrib.auth.models import User, Group
from nosotros.models import Nosotros , Profesional
from rest_framework import serializers
 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfesionalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profesional
        fields = ('nombre' , 'titulo' , 'imagen')

class NosotrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nosotros
        fields = ('titulo' , 'contenido')