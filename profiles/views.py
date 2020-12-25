from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import Profiles
from .serializers import ProfileSerializers
from misc.custom_generic import PartialUpdateAPIView


# Create your views here.

# @csrf_exempt
# @api_view
# def profile_list(request):

#     if request.method =="GET":
#         profiles = Profiles.objects.all()
#         serializers = ProfileSerializers(profiles , many = True)   #many = True ----> several objects
#         return JsonResponse(serializers.data , safe=False)

#     if request.method =="POST":
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data , status=201)  #201----->created
#         return JsonResponse(serializer.errors , status=400)   #400------> bad request




# class ProfilesView(APIView):
#     def get (self , request):
#         profiles = Profiles.objects.all()
#         serializers = ProfileSerializers(profiles , many = True)   #many = True ----> several objects
#         return Response(serializers.data)


class Profilesview (generics.ListCreateAPIView):
    serializer_class = ProfileSerializers
    queryset = Profiles.objects.all()

# class ProfileRetrive (generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProfileSerializers
#     queryset = Profiles.objects.all()


class ProfileRetrive (PartialUpdateAPIView):
    serializer_class = ProfileSerializers
    queryset = Profiles.objects.all()