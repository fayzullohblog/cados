from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Advocate
from .serializer import AdvocateSerializer
# Create your views here.
@api_view(['GET'])
def endpoint(request):
    advocate=Advocate.objects.all()
    serializer=AdvocateSerializer(advocate,many=True)
     
    return Response(data=serializer.data)

     