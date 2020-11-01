from django.shortcuts import render
from rest_framework import status
# Create your views here.
from .serializers import*
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
#from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status, views
from .models import *
from django.db.models import Q
from backend.models import Hospital,Specilization
#from passlib.hash import pbkdf2_sha256

class  RegisterAPI(viewsets.ModelViewSet):
 
    def create(self,request):
        '''Account Details Api'''
        serializer=AccountDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user=serializer.save()
        print('ankur',user)
        return Response({"message":"Data entered successfully","success":"1","data":serializer.data},status=status.HTTP_200_OK)

class List(viewsets.ModelViewSet):
    def list(self,request):
        try:
            total_nurses=f_users.objects.all()
            serializer=AccountDetailSerializer(instance=total_nurses,many=True)
            print(serializer.data)
            return Response({"success":"1","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR',e)
            return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate, login

# class LoginView(views.APIView):

#     def log(self,request):

#         f_users = authenticate(
#         email=request.data.get("email"),
#         password=request.data.get("password"),
#         )
#         if f_users:
#             login(request, f_users)
#             return Response("Log in successfull")
#             # Redirect to a success page.
#             ...
#         else:
#             # Return an 'invalid login' error message.
#             return Response("credentials not match")
#             ...



# class SignUp(viewsets.ModelViewSet):
#     def create(self,request):
#         try:
#             serializer=SignUpSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({"message":"Created successfully",
#                             "success":True,
#                             "address":serializer.data },
#                         status=status.HTTP_200_OK)
#         except Exception as e:
#                 print('ERROR',e)
#                 return Response({"success":False,"message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)

class LoginView(viewsets.ModelViewSet):
    def create(self,request):
        try:
            email=request.data.get('email')
            password=request.data.get('password')
            obj=f_users.objects.filter(Q(email=email)&Q(password=password))
            if obj:
                return Response({"message":"Log In Successfull",
                                "success":"1"},
                            status=status.HTTP_200_OK)
            if not obj:
                return Response({"message":"User Does not Exist",
                                "success":"2"
                                },
                            status=status.HTTP_200_OK)
        except Exception as e:
                print('ERROR',e)
                return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)
############ Get country  by akhil #################
class country(viewsets.ModelViewSet):
    def country(self,request):
        try:
            total_nurses=countries.objects.all()
            serializer=CountrySerializer(instance=total_nurses,many=True)
            print(serializer.data)
            return Response({"success":"1","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR',e)
            return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)
class state(viewsets.ModelViewSet):
    def state(self,request):
        try:
            country_id = request.data.get('country_id')
            state=states.objects.filter(country_id=country_id)
            serializer=StatesSerializer(instance=state,many=True)
            print(serializer.data)
            return Response({"success":"1","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR',e)
            return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)
class city(viewsets.ModelViewSet):
    def city(self,request):
        try:
            state_id = request.data.get('state_id')
            city=cities.objects.filter(state_id=state_id)
            serializer=CitiesSerializer(instance=city,many=True)
            print(serializer.data)
            return Response({"success":"1","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR',e)
            return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)
class hospital(viewsets.ModelViewSet):
    def hospital(self,request):
        try:
            total_nurses=Hospital.objects.all()
            serializer=HospitalSerializer(instance=total_nurses,many=True)
            print(serializer.data)
            return Response({"success":"1","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR',e)
            return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)
class specilization(viewsets.ModelViewSet):
    def specilization(self,request):
        try:
            total_nurses=Specilization.objects.all()
            serializer=SpecilizationSerializer(instance=total_nurses,many=True)
            print(serializer.data)
            return Response({"success":"1","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR',e)
            return Response({"success":"2","message":"Something Went Wrong!"},status=status.HTTP_400_BAD_REQUEST)
############ Get country  by akhil #################