from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Report_db
from .serialize import Report_Serializer
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

class ReportList(APIView):

    def get(self,request):
        report = Report_db.objects.all()
        serializer = Report_Serializer(report,many=True)
        response = {'status':200,'data':serializer.data}
        return JsonResponse(response)

    def post(self,request):
        name = str(request.POST.get('name'))
        phone = str (request.POST.get('phone'))

        check = Report_db.objects.save(name,phone)

        if check :response = {'status':"Added"}
        else     :response = {'status':"Not Added"}

        return JsonResponse(response)
