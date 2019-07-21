from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    #Parecido a django forms
    name = serializers.CharField(max_length=20)
