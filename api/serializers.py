from rest_framework import serializers

from api.models import Pessoa, InfoTable


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class InfoTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoTable
        fields = '__all__'
