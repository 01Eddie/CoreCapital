from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from proyect.models import Person
import json

from django.core import serializers

# Create your views here.
def index(request):
    data = serializers.serialize("json", Person.objects.all())
    # return HttpResponse("Hello, world. You're at the polls index.")
    return JsonResponse({'data': json.loads(data)})
