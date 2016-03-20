from django.shortcuts import render

# Create your views here.
from mufc.models import Mufc
from mufc.serializers import MufcSerializer, ManUtdSerializer
from rest_framework import generics
# from rest_framework.decorators import api_view


def get_serializer_class(self):
    pass


class MufcList(generics.ListCreateAPIView):
    queryset = Mufc.objects.all()
    serializer_class = get_serializer_class

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return MufcSerializer
        return ManUtdSerializer


class MufcDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mufc.objects.all()
    serializer_class = get_serializer_class

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return MufcSerializer
        return ManUtdSerializer
