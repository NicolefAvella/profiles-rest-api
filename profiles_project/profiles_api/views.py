from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    '''Test API View'''
    serializer_class = serializers.HelloSerializer

    def get(sel, request, format=None):
        '''get retorna uno o mas items'''
        an_apiview = ['Practica metodos HTTP']

        return Response({'message':'Hola', 'an_apiview':an_apiview})

    def post(self, request):
        ''' post crea un item'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                )

    def put(self, request, pk=None):
        '''put actualiza un item'''
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        '''path actualiza parcialmente un item'''
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        '''delete borra item'''
        return Response({'method':'DELETE'})
