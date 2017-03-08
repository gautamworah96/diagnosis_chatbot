from rest_framework import serializers
from .models import Main,Userinput


class MainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Main
        fields = ('name','discription','treatment','cause')


class messageSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userinput
        fields = '__all__'
