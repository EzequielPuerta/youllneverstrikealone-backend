from rest_framework_mongoengine.serializers import DocumentSerializer
from gatherings.models import Gatherings


class GatheringSerializer(DocumentSerializer):
    class Meta:
        model = Gatherings
        fields = '__all__'
