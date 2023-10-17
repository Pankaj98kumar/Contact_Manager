from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status

class ContactView(APIView):
    def get(self,request,format=None):
        name = request.query_params.get('name')
        phone = request.query_params.get('phone')

        users = User.objects.all()

        if name:
            users = users.filter(name=name)

        if phone:
            users = users.filter(phone=phone)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'User added to Contacts'},status=status.HTTP_201_CREATED)
    
    def delete(self,request,format=None):
        name = request.query_params.get('name')
        user=User.objects.filter(name=name)
        if len(user) == 0:
            return Response({'msg':'contact not found'})
        user.delete()
        return Response({'msg':'contact deleted'})
