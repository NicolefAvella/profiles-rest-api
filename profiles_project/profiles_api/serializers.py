from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    #Parecido a django forms
    name = serializers.CharField(max_length=20)

class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object'''

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name',  'password') #lista con campos que deseo sean accesibles
        extra_kwargs = {
            'password':{
                'write_only':True,  #para que no pueda ser visible, solo crear o actualizar
                'style':{'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        '''Crea y retorna nuevo usuario'''
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user
