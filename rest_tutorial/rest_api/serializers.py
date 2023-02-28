from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_api.models import Item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ItemSeriealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['ItemId','ItemName', 'Price', 'Quantity', 'Category']