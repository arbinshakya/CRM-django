# from webapp.models import User
from rest_framework import serializers
from webapp.forms import User, Record



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        # fields = ['id','first_name','last_name','gender','email','phone','address','city','province','country']
        fields = '__all__'



