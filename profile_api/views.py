from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profile_api import serializer, models
 

class HelloApiView(APIView):

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """ Retornar lista de caracteristica del APIVIEW"""

        an_apiview = [

            'Usamos metodos Http como funciones (get, post, parch, put, delete)',
             'Es similar a una vista tradicional de Django',
             'Nos da el mayor control sobre la logica de nuestra aplicacion',
             'Esta mapiado manualmente a los URLs',
        ]

        
        # cada funcion http (get, post, parch, put, delete ) que se agregue debe retornar un response object, 
        # esta repuesta va a convertir la informacion en un formato json y debe ser una lista o un diccionario

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name') # es lo que definimos en la clase serializer.py
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    
    def put(self, request, pk=None):
        """ Maneja actualizar un objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualizar parcialmente un objeto"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ borrar un objeto"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializer.HelloSerializer

    def list(self, request):

        a_viewset= [
            'Usa acciones (list, create, retrieve, update, partial_update',
            'Automaticamente mapea a los URLs usando Routers',
            'Provee mas funcionalidad con menos codigo',
        ]

        return Response({'message':'Hola!', 'a_viewset':a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name') # es lo que definimos en la clase serializer.py
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None): # obtiene un objeto y su ID

        return Response({'http_method':'GET'})

    def update(self, request, pk=None): 

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all() # para obtener todos los objetos que han sido creados