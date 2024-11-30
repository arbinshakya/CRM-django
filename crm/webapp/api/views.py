from webapp.models import User, Record
from webapp.api.serializers import UserSerializer, RecordSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import  IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['first_name']
  
