from rest_framework import serializers
from .models import CommonMatchingTable,MasterTable

class MatchingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonMatchingTable
        fields = "__all__"

class MasterTableSerializer(serializers.ModelSerializer):
    # You can include the related CommonMatchingTable serializer if needed
    #is used to handle relationships between models in a serializer.
    type = serializers.PrimaryKeyRelatedField(queryset=CommonMatchingTable.objects.all())
    class Meta:
        model = MasterTable
        fields = ['id', 'type', 'value', 'code', 'created_on', 'updated_on']