from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers

from api.models import InfoTable


class InfoTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoTable
        fields = '__all__'


class InfoTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = getattr(InfoTable, 'objects').all()
    serializer_class = InfoTableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
