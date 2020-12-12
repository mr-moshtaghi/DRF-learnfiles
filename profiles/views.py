from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import Profiles
from .serializers import ProfileSerializers

# Create your views here.

@csrf_exempt
def profile_list(request):

    if request.method =="GET":
        profiles = Profiles.objects.all()
        serializers = ProfileSerializers(profiles , many = True)
        return JsonResponse(serializers.data , safe=False)

    if request.method =="POST":
        data = JSONParser().parse(request)
        serializer = ProfileSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)  #201----->created
        return JsonResponse(serializer.errors , status=400)   #400------> bad request