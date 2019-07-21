from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    '''Test API View'''

    def get(sel, request, format=None):
        '''get retorna uno o mas items'''
        an_apiview = ['Practica metodos HTTP']

        return Response({'message':'Hola', 'an_apiview':an_apiview})
#''' post crea un item'''
#'''put actualiza un item'''
#'''path actualiza parcialmente un item'''
#'''delete borra item'''
