from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Advocate
from .serializer import AdvocateSerializer
from django.db.models import Q
# Create your views here.
@api_view(['GET'])
def endpoint(request):
    query=request.GET.get('username')
    bio=request.GET.get('bio')
    print('---',query)
    if  query==None:
        query=''
    elif bio == None:
        bio=''

    advocate=Advocate.objects.filter(username__icontains=query,bio__icontains=bio)
    serializer=AdvocateSerializer(advocate,many=True)
     
    return Response(data=serializer.data)
@api_view(['GET'])
def advocate_username(request,username):
    advocate_username=[username]
    return Response(advocate_username)
     