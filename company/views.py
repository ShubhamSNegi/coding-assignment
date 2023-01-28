from rest_framework import generics

from .serializers import CompanySerializer
from .models import Company


class CompanyApis(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer