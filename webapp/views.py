from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
#from django.contrib.auth.decorators import login_required
from . models import Patient
from . serializers import PatientSerializer
from . serializers import RecordCreateSerializer
from . serializers import RecordUpdateSerializer
from . serializers import RecordSerializer
from . models import Record
#from . serializers import RecordSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )

from .permissions import IsOwnerOrReadOnly

class PatientList(ListAPIView):
    #if not self.request.user.is_staff or not self.request.user.is_superuser:
    #    raise Http404
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAdminUser]
    

class RecordList(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

class RecordCreateAPIView(CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordCreateSerializer
    lookup_field = 'adhaarId'
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class RecordUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)






    #def post(self):
    #    pass

#class RecordList(APIView):

#    def get(self, request):
#        record1 = Record.objects.all()
#        serializer = RecordSerializer(record1, many=True)
#        return Response(serializer.data)