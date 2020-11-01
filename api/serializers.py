from rest_framework import serializers
from django.contrib.auth.models import User
from.models import*
from backend.models import Specilization,Hospital


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=f_users
        fields=['id','name','email','hospital','speciality','country','city','mobile','created_date','modified_date','password']
        


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = auth_user
#         fields = ('email', 'password')

##########country by akhil ###############
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields = ['id', 'name', 'sortname', 'phonecode']

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = states
        fields = ['id', 'name', 'country_id']

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = cities
        fields = ['id', 'name', 'state_id']

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'title_EN', 'title_AR', 'is_delete']

class SpecilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specilization
        fields = ['id', 'title_EN', 'title_AR', 'is_delete']

##########country by akhil ###############