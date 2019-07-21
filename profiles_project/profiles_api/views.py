from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

from rest_framework import viewsets

# Create your views here.

class HelloApiView(APIView):
    '''Test APIView'''
    serializer_class = serializers.HelloSerializer

    def get(sel, request, format=None):
        '''get retorna uno o mas items'''
        an_apiview = ['Practica metodos HTTP APIView']

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


class HelloViewSet(viewsets.ViewSet):
    '''Test ViewSet'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''list da una lista de objetos, parecido a get'''

        a_viewset = [
            'View Set API para operaciones sencillas'
        ]
        return Response({'message':'Hola', 'a_viewset': a_viewset})

    def create(self, request):
        ''' create crea nuevos objetos'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        ''' retrieve consigue objeto especifico'''
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        '''update actualiza un objeto'''
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        '''partial-update actualiza parcialmente objeto'''
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        '''destroy borra objeto'''
        return Response({'http_method':'DELETE'})
