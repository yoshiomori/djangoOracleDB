from rest_framework import serializers

from api.models import InfoTable


class InfoTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoTable
        fields = '__all__'
