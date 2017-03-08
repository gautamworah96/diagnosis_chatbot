from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Main
from .models import Symptoms
from rest_framework.views import APIView
from .serializer import MainSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import MainSerializer,messageSerialize
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import pymysql.cursors
import json

# Create your views here.

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='disease',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)





class getInfo(APIView):


    def get(self, request, format=None):
        main = Main.objects.all()
        serializer = MainSerializer(main, many=True)
        return Response(serializer.data)



    def post(self, request, format=None):
        requestdata = JSONParser().parse(request)
        entities = "Cancer"
        action = "getCauses"
        if action == "getInfo":
            with connection.cursor() as cursor:
                sql = "select * from main where name = %s"
                cursor.execute(sql,(str(entities)))
                result=cursor.fetchone()
                responsedata ={'description':result['discription']}
                print(responsedata)
                return Response(responsedata, status=status.HTTP_400_BAD_REQUEST)
        if action == "getSymptoms":
            with connection.cursor() as cursor:
                sql = "select * from main where name = %s"
                cursor.execute(sql,(str(entities)))
                result=cursor.fetchone()
                responsedata ={'description':result['cause']}
                print(responsedata)
                return Response(responsedata, status=status.HTTP_400_BAD_REQUEST)
        if action == "getCauses":
            with connection.cursor() as cursor:
                sql = "select * from main where name = %s"
                cursor.execute(sql,(str(entities)))
                result=cursor.fetchone()
                responsedata ={'description':result['treatment']}
                print(responsedata)
                return Response(responsedata, status=status.HTTP_400_BAD_REQUEST)
        if action == "getTreatment":
            with connection.cursor() as cursor:
                sql = "select * from main where name = %s"
                cursor.execute(sql,(str(entities)))
                result=cursor.fetchone()
                responsedata ={'description':result['treatment']}
                print(responsedata)
                return Response(responsedata, status=status.HTTP_400_BAD_REQUEST)
        return Response(requestdata, status=status.HTTP_400_BAD_REQUEST)



