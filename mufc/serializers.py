from rest_framework import serializers
from mufc.models import Mufc


class MufcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mufc
        exclude = ('age', 'club')


class ManUtdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mufc
        fields = ('__all__')