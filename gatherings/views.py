from rest_framework_mongoengine.viewsets import ModelViewSet
from gatherings.serializers import GatheringSerializer
from gatherings.models import Gatherings


class GatheringSet(ModelViewSet):
    lookup_field = 'id'
    serializer_class = GatheringSerializer

    def get_queryset(self):
        return Gatherings.objects.all()
